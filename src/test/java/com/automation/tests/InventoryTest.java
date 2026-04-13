package com.automation.tests;

import com.automation.config.ConfigReader;
import com.automation.pages.CartPage;
import com.automation.pages.InventoryPage;
import com.automation.pages.LoginPage;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

/**
 * Tests for the Inventory/Products screen.
 */
public class InventoryTest extends BaseTest {

    private final ThreadLocal<InventoryPage> inventoryPage = new ThreadLocal<>();

    @BeforeMethod(alwaysRun = true)
    public void loginBeforeTest() {
        InventoryPage page = new LoginPage(getDriver())
                .loginAs(ConfigReader.getUsername(), ConfigReader.getPassword());
        Assert.assertTrue(page.isAt(), "Precondition failed: inventory was not reached");
        inventoryPage.set(page);
    }

    @AfterMethod(alwaysRun = true)
    public void cleanUp() {
        inventoryPage.remove();
    }

    @Test(description = "The inventory page displays at least one product",
          groups = {"smoke"})
    public void testInventorySampleProducts() {
        int count = inventoryPage.get().getProductCount();
        Assert.assertTrue(count > 0, "The inventory is empty");
        extentTest.get().info("Products: " + count);
    }

    @Test(description = "Adding a product to the cart updates the badge",
          groups = {"smoke", "regression"})
    public void testAddProductToCart() {
        InventoryPage page = inventoryPage.get();
        Assert.assertFalse(page.isCartBadgeDisplayed(),
                "The cart badge should not be visible at startup");

        page.addFirstProductToCart();

        Assert.assertTrue(page.isCartBadgeDisplayed(),
                "The shopping cart badge was not updated");
        Assert.assertEquals(page.getCartBadgeCount(), "1",
                "The badge does not show 1 product");

        extentTest.get().info("Product added – badge displays: " + page.getCartBadgeCount());
    }

    @Test(description = "Go to cart from inventory shows added products",
          groups = {"regression"})
    public void testCartNavigation() {
        InventoryPage page = inventoryPage.get();
        page.addFirstProductToCart();
        CartPage cartPage = page.goToCart();

        Assert.assertTrue(cartPage.isAt(), "The cart was not navigated to.");
        Assert.assertEquals(cartPage.getCartItemCount(), 1,
                "The cart should have 1 item");
        Assert.assertTrue(cartPage.isCheckoutButtonDisplayed(),
                "The Checkout button is not visible");
    }
}
