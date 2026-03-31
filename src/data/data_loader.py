"""
Data Loader con Validación
Este módulo carga datos y valida que cumplan con el schema esperado.
"""

import pandas as pd
import yaml
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class DataLoader:
    def __init__(self, config):
        self.config = config
        self.expected_columns = config['data']['expected_columns']
    
    def validate_schema(self, df):
        """Valida que el DataFrame tenga las columnas correctas"""
        actual_columns = set(df.columns)
        expected_columns = set(self.expected_columns)
        
        missing = expected_columns - actual_columns
        if missing:
            raise ValueError(f"Columnas faltantes: {missing}")
        
        logger.info(f"✓ Schema validado correctamente")
        return True
    
    def load_raw_data(self):
        """Carga el dataset Iris desde el archivo CSV"""
        data_path = Path(self.config['data']['raw_path'])
        
        if not data_path.exists():
            raise FileNotFoundError(f"Archivo no encontrado: {data_path}")
        
        logger.info(f"Cargando datos desde: {data_path}")
        df = pd.read_csv(data_path)
        
        logger.info(f"✓ Cargados {len(df)} registros")
        self.validate_schema(df)
        
        return df


def load_config(config_path='config/config.yaml'):
    """Lee el archivo de configuración YAML"""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)
