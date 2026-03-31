"""
Script de Predicción
=====================
Este script demuestra cómo usar el modelo entrenado para hacer
predicciones sobre datos nuevos (simulando producción).
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent / 'src'))

import pandas as pd
import joblib
from data.data_loader import load_config
from data.preprocessing import DataPreprocessor


def predict_new_flower(sepal_length, sepal_width, petal_length, petal_width):
    """
    Predice la especie de una flor nueva basándose en sus mediciones.
    
    Este es el código que correrías en producción cuando llega una
    nueva flor que necesitás clasificar.
    
    Args:
        sepal_length: Largo del sépalo en cm
        sepal_width: Ancho del sépalo en cm
        petal_length: Largo del pétalo en cm
        petal_width: Ancho del pétalo en cm
        
    Returns:
        tuple: (especie_predicha, probabilidades_por_clase)
    """
    # 1. Cargar config
    config = load_config()
    
    # 2. Cargar modelo y preprocessor guardados
    model = joblib.load(config['model']['model_path'])
    preprocessor = joblib.load(config['model']['preprocessor_path'])
    
    # 3. Crear DataFrame con la flor nueva (mismo formato que training)
    new_flower = pd.DataFrame({
        'sepal_length': [sepal_length],
        'sepal_width': [sepal_width],
        'petal_length': [petal_length],
        'petal_width': [petal_width],
        'species': ['unknown']  # Placeholder, no lo usamos
    })
    
    # 4. Preprocesar (aplicar MISMAS transformaciones que en training)
    X_new = new_flower[preprocessor.feature_columns].values
    X_new_scaled = preprocessor.scaler.transform(X_new)
    
    # 5. Hacer predicción
    prediction = model.predict(X_new_scaled)[0]
    probabilities = model.predict_proba(X_new_scaled)[0]
    
    # 6. Convertir número a nombre de especie
    species_name = preprocessor.label_encoder.inverse_transform([prediction])[0]
    species_names = preprocessor.label_encoder.classes_
    
    return species_name, dict(zip(species_names, probabilities))


def main():
    """
    Demo de predicciones con flores de ejemplo.
    """
    print("="*60)
    print("IRIS CLASSIFICATION - PREDICCIÓN DE NUEVAS FLORES")
    print("="*60)
    
    # Ejemplos de flores para clasificar
    # Estos son datos REALES del dataset que el modelo nunca vio durante training
    test_flowers = [
        {
            'name': 'Flor 1',
            'sepal_length': 5.1,
            'sepal_width': 3.5,
            'petal_length': 1.4,
            'petal_width': 0.2,
            'real_species': 'setosa'
        },
        {
            'name': 'Flor 2',
            'sepal_length': 6.7,
            'sepal_width': 3.0,
            'petal_length': 5.2,
            'petal_width': 2.3,
            'real_species': 'virginica'
        },
        {
            'name': 'Flor 3',
            'sepal_length': 5.7,
            'sepal_width': 2.8,
            'petal_length': 4.1,
            'petal_width': 1.3,
            'real_species': 'versicolor'
        }
    ]
    
    # Hacer predicciones
    for flower in test_flowers:
        print(f"\n{flower['name']}:")
        print(f"  Mediciones: sepal_length={flower['sepal_length']}, "
              f"sepal_width={flower['sepal_width']}, "
              f"petal_length={flower['petal_length']}, "
              f"petal_width={flower['petal_width']}")
        
        # Predecir
        predicted_species, probabilities = predict_new_flower(
            flower['sepal_length'],
            flower['sepal_width'],
            flower['petal_length'],
            flower['petal_width']
        )
        
        # Mostrar resultado
        print(f"  Especie real: {flower['real_species']}")
        print(f"  Predicción: {predicted_species}")
        
        # Mostrar confianza del modelo
        print(f"  Probabilidades:")
        for species, prob in probabilities.items():
            print(f"    {species}: {prob*100:.1f}%")
        
        # Indicar si acertó
        is_correct = "✓ CORRECTO" if predicted_species == flower['real_species'] else "✗ INCORRECTO"
        print(f"  {is_correct}")
    
    print("\n" + "="*60)
    print("Predicciones completadas")
    print("="*60)


if __name__ == '__main__':
    main()
