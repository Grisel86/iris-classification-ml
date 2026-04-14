import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.support.locators.RelativeLocator;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
import java.util.List;

public class SeleniumDemo {

    private static final String LOGIN_URL = "https://practicetestautomation.com/practice-test-login/";
    private static final String EXCEPTIONS_URL = "https://practicetestautomation.com/practice-test-exceptions/";
    private static final String VALID_USERNAME = "student";
    private static final String VALID_PASSWORD = "Password123";

    public static void main(String[] args) {
        WebDriver driver = createChromeDriver();
        try {
            findLoginPageElements(driver);
            findExceptionPageElements(driver);
            testValidLogin(driver);
            testInvalidUsernameLogin(driver);
            testInvalidPasswordLogin(driver);
            testEmptyCredentialsLogin(driver);
            testExceptionPageAddRow(driver);
            testExceptionPageEditRow(driver);
            testBrowserNavigation(driver);
            testPageTitle(driver);
            System.out.println("\n=== All test scenarios completed ===");
        } finally {
            driver.quit();
        }
    }

    // =========================================================================
    // ELEMENT LOCATOR DEMOS
    // =========================================================================

    private static void findLoginPageElements(WebDriver driver) {
        driver.get(LOGIN_URL);
        System.out.println("=== Login Page Element Locators ===");

        // Username field — multiple locator strategies
        WebElement usernameById             = driver.findElement(By.id("username"));
        WebElement usernameByXpath          = driver.findElement(By.xpath("//input[@id='username']"));
        WebElement usernameByXpathType      = driver.findElement(By.xpath("//input[@type='text']"));
        WebElement usernameByXpathContains  = driver.findElement(By.xpath("//*[contains(@id,'user')]"));
        WebElement usernameByXpathPlaceholder = driver.findElement(By.xpath("//input[@placeholder='Username']"));
        WebElement usernameByCss            = driver.findElement(By.cssSelector("input[id='username']"));
        WebElement usernameByCssType        = driver.findElement(By.cssSelector("input[type='text']"));
        System.out.println("Username field found: " + usernameById.isDisplayed());

        // Password field — multiple locator strategies
        WebElement passwordByName       = driver.findElement(By.name("password"));
        WebElement passwordByXpath      = driver.findElement(By.xpath("//input[@name='password']"));
        WebElement passwordByXpathType  = driver.findElement(By.xpath("//input[@type='password']"));
        WebElement passwordByCss        = driver.findElement(By.cssSelector("input[name='password']"));
        WebElement passwordByCssType    = driver.findElement(By.cssSelector("input[type='password']"));
        System.out.println("Password field found: " + passwordByName.isDisplayed());

        // Submit button — multiple locator strategies
        WebElement submitByClass     = driver.findElement(By.className("btn"));
        WebElement submitByXpath     = driver.findElement(By.xpath("//button[@id='submit']"));
        WebElement submitByXpathText = driver.findElement(By.xpath("//button[text()='Submit']"));
        WebElement submitByCss       = driver.findElement(By.cssSelector("button[id='submit']"));
        WebElement submitByCssClass  = driver.findElement(By.cssSelector("button.btn"));
        System.out.println("Submit button found: " + submitByClass.isDisplayed());

        // Tag-based collection of all inputs
        List<WebElement> inputFields = driver.findElements(By.tagName("input"));
        System.out.println("Total input fields on page: " + inputFields.size());

        // Link locators
        WebElement linkByText        = driver.findElement(By.linkText("Practice Test Automation."));
        WebElement linkByPartialText = driver.findElement(By.partialLinkText("Test Automation"));
        System.out.println("Footer link found: " + linkByText.isDisplayed());

        // Relative locators
        WebElement passwordBelowUsername = driver.findElement(
                RelativeLocator.with(By.tagName("input")).below(By.id("username")));
        WebElement privacyPolicyLink = driver.findElement(
                RelativeLocator.with(By.tagName("a")).toRightOf(By.partialLinkText("Test Automation")));
        System.out.println("Password (below username via relative locator) found: "
                + passwordBelowUsername.isDisplayed());

        // Navigation menu
        WebElement homeButton = driver.findElement(By.className("menu-item-home"));
        System.out.println("Home menu item found: " + homeButton.isDisplayed());
    }

    private static void findExceptionPageElements(WebDriver driver) {
        driver.get(EXCEPTIONS_URL);
        System.out.println("\n=== Exceptions Page Element Locators ===");

        // Link to course — full and partial link text
        WebElement courseLink        = driver.findElement(By.linkText("Selenium WebDriver with Java for beginners program"));
        WebElement courseLinkPartial = driver.findElement(By.partialLinkText("Selenium WebDriver"));
        System.out.println("Course link found: " + courseLink.isDisplayed());

        // Row 1 input field — tag, class name, XPath, CSS
        WebElement inputByTag   = driver.findElement(By.tagName("input"));
        WebElement inputByClass = driver.findElement(By.className("input-field"));
        WebElement inputByXpath = driver.findElement(By.xpath("//div[@id='row1']//input"));
        WebElement inputByCss   = driver.findElement(By.cssSelector("div#row1 input"));
        System.out.println("Row 1 input found: " + inputByTag.isDisplayed());

        // All buttons as a collection
        List<WebElement> allButtons = driver.findElements(By.tagName("button"));
        System.out.println("Total buttons found: " + allButtons.size());

        // "Add" button — ID, name, CSS, XPath
        WebElement addButtonById    = driver.findElement(By.id("add_btn"));
        WebElement addButtonByName  = driver.findElement(By.name("add_btn"));
        WebElement addButtonByCss   = driver.findElement(By.cssSelector("button#add_btn"));
        WebElement addButtonByXpath = driver.findElement(By.xpath("//button[@id='add_btn']"));
        System.out.println("Add button found: " + addButtonById.isDisplayed());

        // "Edit" button — ID, name, CSS, XPath  (may be hidden; getAttribute checks its style)
        WebElement editButtonById    = driver.findElement(By.id("edit_btn"));
        WebElement editButtonByName  = driver.findElement(By.name("edit_btn"));
        WebElement editButtonByCss   = driver.findElement(By.cssSelector("button#edit_btn"));
        WebElement editButtonByXpath = driver.findElement(By.xpath("//button[@id='edit_btn']"));
        System.out.println("Edit button located (visibility style): "
                + editButtonById.getAttribute("style"));
    }

    // =========================================================================
    // TEST SCENARIOS — Login Page
    // =========================================================================

    /** Scenario 1: Valid credentials → success page. */
    private static void testValidLogin(WebDriver driver) {
        driver.get(LOGIN_URL);
        System.out.println("\n=== Test 1: Valid Login ===");

        driver.findElement(By.id("username")).sendKeys(VALID_USERNAME);
        driver.findElement(By.name("password")).sendKeys(VALID_PASSWORD);
        driver.findElement(By.id("submit")).click();

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(5));
        WebElement heading = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.className("post-title")));

        boolean passed = heading.getText().contains("Logged In Successfully");
        System.out.println("Result: " + (passed ? "PASS" : "FAIL") + " | Heading: " + heading.getText());
    }

    /** Scenario 2: Wrong username → "Your username is invalid!" error. */
    private static void testInvalidUsernameLogin(WebDriver driver) {
        driver.get(LOGIN_URL);
        System.out.println("\n=== Test 2: Invalid Username ===");

        driver.findElement(By.id("username")).sendKeys("wronguser");
        driver.findElement(By.name("password")).sendKeys(VALID_PASSWORD);
        driver.findElement(By.id("submit")).click();

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(5));
        WebElement error = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.id("error")));

        boolean passed = error.getText().contains("Your username is invalid!");
        System.out.println("Result: " + (passed ? "PASS" : "FAIL") + " | Error: " + error.getText());
    }

    /** Scenario 3: Wrong password → "Your password is invalid!" error. */
    private static void testInvalidPasswordLogin(WebDriver driver) {
        driver.get(LOGIN_URL);
        System.out.println("\n=== Test 3: Invalid Password ===");

        driver.findElement(By.id("username")).sendKeys(VALID_USERNAME);
        driver.findElement(By.name("password")).sendKeys("wrongpass");
        driver.findElement(By.id("submit")).click();

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(5));
        WebElement error = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.id("error")));

        boolean passed = error.getText().contains("Your password is invalid!");
        System.out.println("Result: " + (passed ? "PASS" : "FAIL") + " | Error: " + error.getText());
    }

    /** Scenario 4: Empty credentials → error message shown. */
    private static void testEmptyCredentialsLogin(WebDriver driver) {
        driver.get(LOGIN_URL);
        System.out.println("\n=== Test 4: Empty Credentials ===");

        // Submit without filling in any fields
        driver.findElement(By.id("submit")).click();

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(5));
        WebElement error = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.id("error")));

        boolean passed = !error.getText().isEmpty();
        System.out.println("Result: " + (passed ? "PASS" : "FAIL") + " | Error: " + error.getText());
    }

    // =========================================================================
    // TEST SCENARIOS — Exceptions Page
    // =========================================================================

    /** Scenario 5: Click "Add" → second row input becomes visible and accepts text. */
    private static void testExceptionPageAddRow(WebDriver driver) {
        driver.get(EXCEPTIONS_URL);
        System.out.println("\n=== Test 5: Exception Page — Add Row ===");

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

        driver.findElement(By.id("add_btn")).click();
        WebElement row2Input = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.xpath("//div[@id='row2']//input")));

        row2Input.sendKeys("Added Value");
        boolean passed = "Added Value".equals(row2Input.getAttribute("value"));
        System.out.println("Result: " + (passed ? "PASS" : "FAIL")
                + " | Row 2 value: " + row2Input.getAttribute("value"));
    }

    /** Scenario 6: Click "Edit" on row 1 → input becomes editable → save persists new value. */
    private static void testExceptionPageEditRow(WebDriver driver) {
        driver.get(EXCEPTIONS_URL);
        System.out.println("\n=== Test 6: Exception Page — Edit Row ===");

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

        WebElement editButton = wait.until(
                ExpectedConditions.elementToBeClickable(By.id("edit_btn")));
        editButton.click();

        WebElement row1Input = wait.until(
                ExpectedConditions.elementToBeClickable(By.xpath("//div[@id='row1']//input")));
        row1Input.clear();
        row1Input.sendKeys("Edited Value");

        WebElement saveButton = wait.until(
                ExpectedConditions.elementToBeClickable(By.id("save_btn")));
        saveButton.click();

        WebElement row1 = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.id("row1")));
        boolean passed = row1.getText().contains("Edited Value");
        System.out.println("Result: " + (passed ? "PASS" : "FAIL")
                + " | Row 1 text: " + row1.getText());
    }

    // =========================================================================
    // TEST SCENARIOS — Browser Navigation
    // =========================================================================

    /** Scenario 7: Navigate back, forward, and refresh using the browser API. */
    private static void testBrowserNavigation(WebDriver driver) {
        System.out.println("\n=== Test 7: Browser Navigation ===");

        driver.get(LOGIN_URL);
        driver.get(EXCEPTIONS_URL);

        driver.navigate().back();
        boolean backPassed = driver.getCurrentUrl().contains("practice-test-login");
        System.out.println("Navigate Back:    " + (backPassed ? "PASS" : "FAIL")
                + " | URL: " + driver.getCurrentUrl());

        driver.navigate().forward();
        boolean forwardPassed = driver.getCurrentUrl().contains("practice-test-exceptions");
        System.out.println("Navigate Forward: " + (forwardPassed ? "PASS" : "FAIL")
                + " | URL: " + driver.getCurrentUrl());

        String titleBeforeRefresh = driver.getTitle();
        driver.navigate().refresh();
        boolean refreshPassed = driver.getTitle().equals(titleBeforeRefresh);
        System.out.println("Navigate Refresh: " + (refreshPassed ? "PASS" : "FAIL")
                + " | Title: " + driver.getTitle());
    }

    /** Scenario 8: Verify page titles for both practice pages. */
    private static void testPageTitle(WebDriver driver) {
        System.out.println("\n=== Test 8: Page Titles ===");

        driver.get(LOGIN_URL);
        boolean loginTitlePassed = driver.getTitle().contains("Practice Test Login");
        System.out.println("Login page title:      " + (loginTitlePassed ? "PASS" : "FAIL")
                + " | Title: " + driver.getTitle());

        driver.get(EXCEPTIONS_URL);
        boolean exceptionsTitlePassed = driver.getTitle().contains("Practice Test Exceptions");
        System.out.println("Exceptions page title: " + (exceptionsTitlePassed ? "PASS" : "FAIL")
                + " | Title: " + driver.getTitle());
    }

    // =========================================================================
    // BROWSER FACTORY HELPERS
    // =========================================================================

    /**
     * Creates a ChromeDriver instance. Uncomment the headless argument to run
     * without opening a visible browser window (useful in CI environments).
     */
    private static WebDriver createChromeDriver() {
        ChromeOptions options = new ChromeOptions();
        // options.addArguments("--headless=new");
        return new ChromeDriver(options);
    }

    /**
     * Creates a FirefoxDriver instance. No manual geckodriver path is required
     * when using Selenium Manager (Selenium 4.6+), which resolves the driver
     * automatically on all platforms.
     */
    private static WebDriver createFirefoxDriver() {
        FirefoxOptions options = new FirefoxOptions();
        // options.addArguments("-headless");
        return new FirefoxDriver(options);
    }

    /** Returns the page title when loaded in Chrome. */
    private static String chromeTest(String url) {
        WebDriver driver = createChromeDriver();
        try {
            driver.get(url);
            return driver.getTitle();
        } finally {
            driver.quit();
        }
    }

    /** Returns the page title when loaded in Firefox. */
    private static String firefoxTest(String url) {
        WebDriver driver = createFirefoxDriver();
        try {
            driver.get(url);
            return driver.getTitle();
        } finally {
            driver.quit();
        }
    }
}
