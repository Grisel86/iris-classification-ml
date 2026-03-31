"""
Test del módulo de preprocessing
Estos tests validan que las transformaciones funcionen correctamente.
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

import pandas as pd
import numpy as np
from data.preprocessing import DataPreprocessor


def test_preprocessing_shape():
    """
    Test: El preprocessing debe mantener el número de filas.
    
    En QA esto sería como verificar que tu script de automation
    procese todos los test cases y no se salte ninguno.
    """
    # Arrange (preparar datos de prueba)
    config = {
        'preprocessing': {'scaling_method': 'standard'}
    }
    df = pd.DataFrame({
        'sepal_length': [5.1, 4.9, 4.7],
        'sepal_width': [3.5, 3.0, 3.2],
        'petal_length': [1.4, 1.4, 1.3],
        'petal_width': [0.2, 0.2, 0.2],
        'species': ['setosa', 'setosa', 'setosa']
    })
    
    # Act (ejecutar la función a testear)
    preprocessor = DataPreprocessor(config)
    X, y = preprocessor.fit_transform(df)
    
    # Assert (verificar resultados)
    assert X.shape[0] == 3, f"Se esperaban 3 filas, se obtuvieron {X.shape[0]}"
    assert X.shape[1] == 4, f"Se esperaban 4 features, se obtuvieron {X.shape[1]}"
    assert len(y) == 3, f"Se esperaban 3 labels, se obtuvieron {len(y)}"
    
    print("✓ test_preprocessing_shape PASSED")


def test_labels_encoding():
    """
    Test: Las especies deben convertirse a números 0, 1, 2.
    
    Esto valida que la transformación de labels funcione correctamente.
    """
    # Arrange
    config = {'preprocessing': {'scaling_method': 'standard'}}
    df = pd.DataFrame({
        'sepal_length': [5.1, 5.9, 6.5],
        'sepal_width': [3.5, 3.0, 3.0],
        'petal_length': [1.4, 4.2, 5.5],
        'petal_width': [0.2, 1.5, 2.1],
        'species': ['setosa', 'versicolor', 'virginica']
    })
    
    # Act
    preprocessor = DataPreprocessor(config)
    X, y = preprocessor.fit_transform(df)
    
    # Assert
    assert set(y) == {0, 1, 2}, f"Labels encoded incorrectamente: {set(y)}"
    assert len(np.unique(y)) == 3, "Deben haber exactamente 3 clases"
    
    print("✓ test_labels_encoding PASSED")


def test_scaling_mean_zero():
    """
    Test: Después de StandardScaler, la media debe ser aproximadamente 0.
    
    Este test valida que el scaling esté funcionando correctamente.
    """
    # Arrange
    config = {'preprocessing': {'scaling_method': 'standard'}}
    df = pd.DataFrame({
        'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0],
        'sepal_width': [3.5, 3.0, 3.2, 3.1, 3.6],
        'petal_length': [1.4, 1.4, 1.3, 1.5, 1.4],
        'petal_width': [0.2, 0.2, 0.2, 0.2, 0.2],
        'species': ['setosa'] * 5
    })
    
    # Act
    preprocessor = DataPreprocessor(config)
    X, y = preprocessor.fit_transform(df)
    
    # Assert
    means = X.mean(axis=0)
    for i, mean in enumerate(means):
        assert abs(mean) < 1e-10, f"Feature {i} tiene media {mean}, debería ser ~0"
    
    print("✓ test_scaling_mean_zero PASSED")


def run_all_tests():
    """
    Ejecuta todos los tests.
    Esto es como tu test runner en pytest o unittest.
    """
    print("="*50)
    print("EJECUTANDO TESTS DE PREPROCESSING")
    print("="*50)
    
    tests = [
        test_preprocessing_shape,
        test_labels_encoding,
        test_scaling_mean_zero
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} ERROR: {e}")
            failed += 1
    
    print("\n" + "="*50)
    print(f"RESULTADOS: {passed} passed, {failed} failed")
    print("="*50)
    
    return failed == 0


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
