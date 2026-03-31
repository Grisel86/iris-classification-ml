"""
Model Evaluation Module
Este módulo evalúa el performance del modelo entrenado.
"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report, confusion_matrix
import logging

logger = logging.getLogger(__name__)


def evaluate_model(model, X_test, y_test, config):
    """
    Evalúa el modelo y genera métricas de performance.
    
    Esto es como tu test report en QA: te dice qué tan bien está funcionando.
    
    Args:
        model: Modelo entrenado
        X_test: Features de test
        y_test: Labels reales de test
        config: Configuración con métricas y umbrales
        
    Returns:
        dict con todas las métricas calculadas
    """
    logger.info("Evaluando modelo...")
    
    # Hacer predicciones
    y_pred = model.predict(X_test)
    
    # Calcular métricas
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted'),
        'recall': recall_score(y_test, y_pred, average='weighted'),
        'f1_score': f1_score(y_test, y_pred, average='weighted')
    }
    
    # Log de resultados
    logger.info("="*50)
    logger.info("MÉTRICAS DEL MODELO")
    logger.info("="*50)
    for metric_name, metric_value in metrics.items():
        logger.info(f"{metric_name}: {metric_value:.4f}")
    
    # Quality Gate (concepto de QA aplicado a ML)
    min_accuracy = config['evaluation']['min_accuracy']
    if metrics['accuracy'] < min_accuracy:
        logger.warning(f"⚠ QUALITY GATE FAILED: Accuracy {metrics['accuracy']:.4f} < threshold {min_accuracy}")
    else:
        logger.info(f"✓ QUALITY GATE PASSED: Accuracy {metrics['accuracy']:.4f} >= threshold {min_accuracy}")
    
    # Reporte detallado por clase
    logger.info("\nReporte de clasificación por clase:")
    logger.info("\n" + classification_report(y_test, y_pred))
    
    # Matriz de confusión
    cm = confusion_matrix(y_test, y_pred)
    logger.info("\nMatriz de Confusión:")
    logger.info(str(cm))
    
    return metrics


def validate_predictions(y_pred, y_test):
    """
    Validaciones adicionales de sanity check.
    
    En QA harías estos checks para asegurarte que los outputs tienen sentido.
    
    Args:
        y_pred: Predicciones del modelo
        y_test: Labels reales
        
    Returns:
        bool: True si pasa todas las validaciones
    """
    # Check 1: Mismo número de predicciones que labels
    if len(y_pred) != len(y_test):
        logger.error(f"ERROR: Número de predicciones ({len(y_pred)}) != labels ({len(y_test)})")
        return False
    
    # Check 2: Predicciones en el rango válido
    if y_pred.min() < 0 or y_pred.max() > 2:
        logger.error(f"ERROR: Predicciones fuera de rango: min={y_pred.min()}, max={y_pred.max()}")
        return False
    
    logger.info("✓ Todas las validaciones de sanity check pasaron")
    return True
