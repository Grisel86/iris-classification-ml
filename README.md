# Iris Classification - ML End-to-End Project

Proyecto de clasificación de flores Iris que demuestra una arquitectura ML profesional con separación de concerns, testing, y reproducibilidad.

**Autor:** Fabiana Grisel González  
**Fecha:** Marzo 2026  
**Dataset:** Iris Flower Classification (150 samples, 3 especies)

---

## 🎯 Objetivo del Proyecto

Construir un clasificador de flores Iris que:
- Sea **reproducible** (cualquiera puede ejecutarlo y obtener los mismos resultados)
- Sea **testeable** (con tests automatizados)
- Sea **mantenible** (código organizado y modular)
- Esté listo para **deployment** (con Quality Gates y validaciones)

---

## 📁 Estructura del Proyecto

```
iris-classification-project/
├── config/
│   └── config.yaml              # Configuración centralizada
├── data/
│   ├── raw/                     # Datos originales (inmutables)
│   └── processed/               # Datos procesados
├── models/
│   ├── iris_model.pkl          # Modelo entrenado
│   └── preprocessor.pkl        # Preprocessor con transformaciones
├── notebooks/                   # Exploración (futuro)
├── src/
│   ├── data/
│   │   ├── data_loader.py      # Carga y validación de datos
│   │   └── preprocessing.py    # Transformaciones de datos
│   ├── models/
│   │   ├── train.py            # Entrenamiento de modelos
│   │   └── evaluate.py         # Evaluación y métricas
│   └── utils/
├── tests/
│   └── test_preprocessing.py   # Tests unitarios
├── logs/
│   └── training.log            # Logs de ejecución
└── main.py                      # Pipeline principal

```

---

## 🚀 Cómo Usar Este Proyecto

### 1. Ejecutar el pipeline completo

```bash
python3 main.py
```

Esto ejecuta todo el flujo end-to-end:
- Carga datos
- Preprocesa
- Entrena modelo
- Evalúa performance
- Reporta métricas

**Salida esperada:**
```
Accuracy: 0.9333
Precision: 0.9333
Recall: 0.9333
F1-Score: 0.9333
✓ QUALITY GATE: PASSED
```

### 2. Ejecutar tests

```bash
python3 tests/test_preprocessing.py
```

Esto ejecuta todos los tests unitarios para validar que los componentes funcionen correctamente.

### 3. Modificar configuración

Edita `config/config.yaml` para experimentar con diferentes parámetros:

```yaml
model:
  algorithm: "RandomForest"  # Cambiar a "LogisticRegression" o "DecisionTree"
  parameters:
    n_estimators: 100        # Cambiar número de árboles
    max_depth: 5             # Cambiar profundidad
```

Después simplemente volvé a ejecutar `python3 main.py`.

---

## 📊 Resultados del Modelo

### Métricas de Performance

| Métrica | Valor |
|---------|-------|
| Accuracy | 93.33% |
| Precision | 93.33% |
| Recall | 93.33% |
| F1-Score | 93.33% |

### Performance por Clase

| Especie | Precision | Recall | F1-Score |
|---------|-----------|--------|----------|
| Setosa | 100% | 100% | 100% |
| Versicolor | 90% | 90% | 90% |
| Virginica | 90% | 90% | 90% |

### Matriz de Confusión

```
          Predicho
Real    setosa  versicolor  virginica
setosa    10       0           0
versicolor 0       9           1
virginica  0       1           9
```

**Interpretación:** El modelo clasificó perfectamente todas las flores Setosa, pero confundió 1 Versicolor con Virginica y 1 Virginica con Versicolor (2 errores en 30 predicciones).

---

## 🔍 Conceptos Clave del Proyecto

### 1. Separación de Datos
- **data/raw/** - Datos originales que NUNCA se modifican
- **data/processed/** - Datos transformados, pueden regenerarse

### 2. Fit vs Transform
- **fit_transform()** - Aprende parámetros del train set (media, std, etc.)
- **transform()** - Aplica parámetros ya aprendidos (test set y producción)

### 3. Quality Gate
- Umbral mínimo de accuracy: 85%
- Si el modelo no alcanza este umbral, el pipeline falla
- Concepto tomado de QA/DevOps aplicado a ML

### 4. Reproducibilidad
- `random_state=42` en todos los componentes aleatorios
- Configuración centralizada en YAML
- Logs detallados de cada ejecución

---

## 🧪 Testing

Este proyecto incluye tests automatizados que validan:

1. **test_preprocessing_shape**: Verifica que no se pierdan filas durante el preprocessing
2. **test_labels_encoding**: Valida que las especies se conviertan correctamente a números
3. **test_scaling_mean_zero**: Confirma que el StandardScaler funcione correctamente

**Para agregar más tests:** Crear archivos `test_*.py` en la carpeta `tests/`.

---

## 📦 Artefactos Generados

Después de ejecutar el pipeline, se generan:

1. **models/iris_model.pkl** (160 KB)
   - Modelo RandomForest entrenado
   - Listo para hacer predicciones en producción

2. **models/preprocessor.pkl** (1.9 KB)
   - Scaler y encoder con transformaciones aprendidas
   - Necesario para procesar datos nuevos

3. **logs/training.log**
   - Log completo de la ejecución
   - Incluye timestamps y métricas

---

## 🔮 Próximos Pasos

- [ ] Agregar más tests (para train.py, evaluate.py)
- [ ] Crear notebook de EDA (Exploratory Data Analysis)
- [ ] Implementar cross-validation
- [ ] Crear API REST con FastAPI para predictions
- [ ] Agregar GitHub Actions para CI/CD
- [ ] Dockerizar el proyecto

---

## 💡 Notas para Data Science Interview

Este proyecto demuestra:
- ✅ Arquitectura modular y mantenible
- ✅ Separación de experimentación (notebooks) vs producción (src/)
- ✅ Testing automatizado
- ✅ Quality Gates y validaciones
- ✅ Reproducibilidad garantizada
- ✅ Logging y trazabilidad completa

---

## 📝 Licencia

Este es un proyecto educativo de portfolio.

---

## 👤 Contacto

**Fabiana Grisel González**
- GitHub: [Grisel86](https://github.com/Grisel86)
- LinkedIn: [fabiana-grisel-gonzalez](https://www.linkedin.com/in/fabiana-grisel-gonzalez)
