"""
Model Training Module
Este módulo maneja el entrenamiento del modelo.
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import joblib
import logging

logger = logging.getLogger(__name__)


def get_model(config):
    """
    Crea el modelo según la configuración.
    
    Esto es como un factory pattern que usarías en automation:
    según el config, instanciamos diferentes tipos de modelos.
    
    Args:
        config: Configuración con algorithm y parameters
        
    Returns:
        modelo instanciado sin entrenar
    """
    algorithm = config['model']['algorithm']
    params = config['model']['parameters']
    
    models = {
        'RandomForest': RandomForestClassifier,
        'LogisticRegression': LogisticRegression,
        'DecisionTree': DecisionTreeClassifier
    }
    
    if algorithm not in models:
        raise ValueError(f"Algoritmo no soportado: {algorithm}")
    
    model = models[algorithm](**params)
    logger.info(f"✓ Modelo creado: {algorithm} con parámetros {params}")
    
    return model


def train_model(X_train, y_train, config):
    """
    Entrena el modelo con datos de entrenamiento.
    
    Args:
        X_train: Features de entrenamiento
        y_train: Labels de entrenamiento
        config: Configuración del proyecto
        
    Returns:
        modelo entrenado
    """
    logger.info("Iniciando entrenamiento del modelo...")
    
    # Crear modelo
    model = get_model(config)
    
    # Entrenar
    model.fit(X_train, y_train)
    logger.info("✓ Modelo entrenado exitosamente")

    # Guardar modelo
    from pathlib import Path

    model_path = config['model']['model_path']

    # Crear el directorio si no existe
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, model_path)
    logger.info(f"✓ Modelo guardado en: {model_path}")
    
    return model


def load_model(model_path):
    """
    Carga un modelo previamente entrenado.
    
    Esto es lo que usarías en producción para hacer predicciones.
    """
    model = joblib.load(model_path)
    logger.info(f"✓ Modelo cargado desde: {model_path}")
    return model
