"""
Preprocessing Module
Este módulo maneja todas las transformaciones de datos.
La clave es que las transformaciones se APRENDEN del train set y luego
se APLICAN al test set y a datos nuevos.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
import logging

logger = logging.getLogger(__name__)


class DataPreprocessor:
    """
    Preprocesa datos de manera reproducible.
    
    Concepto clave: fit_transform() aprende y aplica transformaciones al train set.
    transform() solo aplica lo ya aprendido (para test set y datos nuevos).
    
    Esto es como cuando configurabas tu framework de automation:
    el setup se hace una vez, luego lo reutilizás en todos los tests.
    """
    
    def __init__(self, config):
        self.config = config
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        self.feature_columns = None
        
    def fit_transform(self, df):
        """
        Aprende las transformaciones y las aplica (solo en train set).
        
        Args:
            df: DataFrame con features y target
            
        Returns:
            X, y: Features transformadas y labels encoded
        """
        logger.info("Iniciando preprocessing (fit_transform)...")
        
        # Separar features y target
        self.feature_columns = [col for col in df.columns if col != 'species']
        X = df[self.feature_columns].values
        y = df['species'].values
        
        # Encode labels (convertir especies a números: setosa=0, versicolor=1, virginica=2)
        y_encoded = self.label_encoder.fit_transform(y)
        logger.info(f"✓ Labels encoded. Clases: {self.label_encoder.classes_}")
        
        # Scale features (estandarizar features a media=0, std=1)
        X_scaled = self.scaler.fit_transform(X)
        logger.info(f"✓ Features escaladas con {self.config['preprocessing']['scaling_method']} scaler")
        
        return X_scaled, y_encoded
    
    def transform(self, df):
        """
        Aplica transformaciones YA APRENDIDAS (para test set o datos nuevos).
        
        IMPORTANTE: No usar fit_transform acá, solo transform.
        Si usás fit_transform en test set, estás "haciendo trampa" (data leakage).
        
        Args:
            df: DataFrame con las mismas columnas que el train set
            
        Returns:
            X, y: Features transformadas y labels encoded
        """
        logger.info("Aplicando preprocessing (transform)...")
        
        X = df[self.feature_columns].values
        y = df['species'].values
        
        # Aplicar transformaciones ya aprendidas
        y_encoded = self.label_encoder.transform(y)
        X_scaled = self.scaler.transform(X)
        
        logger.info("✓ Transformaciones aplicadas")
        return X_scaled, y_encoded
    
    def save(self, path):
        """Guarda el preprocessor para usarlo después en producción"""
        joblib.dump(self, path)
        logger.info(f"✓ Preprocessor guardado en: {path}")
    
    @staticmethod
    def load(path):
        """Carga un preprocessor guardado"""
        return joblib.load(path)


def split_data(df, config):
    """
    Divide datos en train y test sets.
    
    Args:
        df: DataFrame completo
        config: Configuración con test_size y random_state
        
    Returns:
        train_df, test_df: DataFrames separados
    """
    test_size = config['data']['test_size']
    random_state = config['data']['random_state']
    
    train_df, test_df = train_test_split(
        df, 
        test_size=test_size, 
        random_state=random_state,
        stratify=df['species']  # Mantiene proporción de clases en ambos sets
    )
    
    logger.info(f"✓ Datos divididos: {len(train_df)} train, {len(test_df)} test")
    return train_df, test_df
