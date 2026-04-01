"""
Main Pipeline
Este es el punto de entrada del proyecto.
Orquesta todo el flujo: carga → preprocesamiento → entrenamiento → evaluación.
"""

import sys
import logging
from pathlib import Path

# Agregar src al path para poder importar módulos
sys.path.append(str(Path(__file__).parent / 'src'))

from data.data_loader import DataLoader, load_config
from data.preprocessing import DataPreprocessor, split_data
from models.train import train_model
from models.evaluate import evaluate_model, validate_predictions


def setup_logging(config):
    """
    Configura el sistema de logging.

    Esto es como configurar tu test runner para que genere logs detallados.
    """
    # Crear la carpeta de logs si no existe
    # Esto es importante para CI/CD donde empezamos con un ambiente limpio
    log_file = config['logging']['log_file']
    log_dir = Path(log_file).parent  # Obtiene el directorio del archivo de log
    log_dir.mkdir(parents=True, exist_ok=True)  # Crea el directorio si no existe

    logging.basicConfig(
        level=config['logging']['level'],
        format=config['logging']['format'],
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()  # También imprime en consola
        ]
    )


def main():
    """
    Pipeline principal que ejecuta todo el flujo end-to-end.
    
    Pensalo como un test suite que ejecuta todos los tests en orden.
    """
    print("="*60)
    print("IRIS CLASSIFICATION - PIPELINE END-TO-END")
    print("="*60)
    
    # 1. Cargar configuración
    print("\n[1/6] Cargando configuración...")
    config = load_config()
    setup_logging(config)
    logger = logging.getLogger(__name__)
    logger.info("Pipeline iniciado")
    
    # 2. Cargar datos
    print("[2/6] Cargando y validando datos...")
    loader = DataLoader(config)
    df = loader.load_raw_data()
    logger.info(f"Dataset shape: {df.shape}")
    
    # 3. Split train/test
    print("[3/6] Dividiendo datos en train y test...")
    train_df, test_df = split_data(df, config)
    logger.info(f"Train: {len(train_df)}, Test: {len(test_df)}")
    
    # 4. Preprocessing
    print("[4/6] Preprocesando datos...")
    preprocessor = DataPreprocessor(config)
    
    # Fit en train (aprender transformaciones)
    X_train, y_train = preprocessor.fit_transform(train_df)
    logger.info(f"Train features shape: {X_train.shape}")
    
    # Transform en test (aplicar transformaciones ya aprendidas)
    X_test, y_test = preprocessor.transform(test_df)
    logger.info(f"Test features shape: {X_test.shape}")
    
    # Guardar preprocessor para usar en producción
    preprocessor.save(config['model']['preprocessor_path'])
    
    # 5. Entrenamiento
    print("[5/6] Entrenando modelo...")
    model = train_model(X_train, y_train, config)
    
    # 6. Evaluación
    print("[6/6] Evaluando modelo...")
    y_pred = model.predict(X_test)
    
    # Sanity checks
    if not validate_predictions(y_pred, y_test):
        logger.error("Validación de predicciones FALLÓ")
        return 1
    
    # Calcular métricas
    metrics = evaluate_model(model, X_test, y_test, config)
    
    # Resultado final
    print("\n" + "="*60)
    print("PIPELINE COMPLETADO EXITOSAMENTE")
    print("="*60)
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"Precision: {metrics['precision']:.4f}")
    print(f"Recall: {metrics['recall']:.4f}")
    print(f"F1-Score: {metrics['f1_score']:.4f}")
    
    # Quality Gate
    if metrics['accuracy'] >= config['evaluation']['min_accuracy']:
        print("\n✓ QUALITY GATE: PASSED")
        return 0
    else:
        print("\n✗ QUALITY GATE: FAILED")
        return 1


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
