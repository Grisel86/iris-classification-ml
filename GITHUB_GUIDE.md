# Guía: Subir el Proyecto a GitHub y Configurar CI/CD

## 📋 Prerequisitos

- Tener Git instalado
- Tener una cuenta de GitHub
- Haber descargado y descomprimido el proyecto

---

## 🚀 Paso 1: Subir el Proyecto a GitHub

### 1.1 Crear repositorio en GitHub

1. Ir a https://github.com/new
2. Nombre: `iris-classification-ml`
3. Descripción: `End-to-end ML project for Iris flower classification with production-ready architecture`
4. **NO marcar** "Add README" (ya tenemos uno)
5. Hacer clic en "Create repository"

### 1.2 Inicializar Git localmente

```bash
cd iris-classification-project

# Inicializar Git
git init

# Agregar todos los archivos
git add .

# Hacer primer commit
git commit -m "Initial commit: Complete ML project structure

- Config-driven architecture
- Modular code (data loading, preprocessing, training, evaluation)
- Automated testing
- Quality Gates
- Production-ready predict script
- Comprehensive documentation"

# Conectar con GitHub (reemplazar 'Grisel86' con tu username)
git remote add origin https://github.com/Grisel86/iris-classification-ml.git

# Subir código
git branch -M main
git push -u origin main
```

---

## 🔄 Paso 2: Configurar GitHub Actions para CI/CD

### 2.1 Crear el workflow de CI

Crear el archivo `.github/workflows/ci.yml`:

```bash
mkdir -p .github/workflows
```

Contenido del archivo `.github/workflows/ci.yml`:

```yaml
name: CI Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        python tests/test_preprocessing.py
    
    - name: Run full pipeline
      run: |
        python main.py
    
    - name: Check Quality Gate
      run: |
        if [ $? -eq 0 ]; then
          echo "✓ Quality Gate PASSED"
        else
          echo "✗ Quality Gate FAILED"
          exit 1
        fi
```

### 2.2 Subir el workflow

```bash
git add .github/
git commit -m "Add CI/CD pipeline with GitHub Actions

- Automated testing on push and PR
- Full pipeline execution
- Quality Gate validation"
git push
```

### 2.3 Verificar que funciona

1. Ir a tu repositorio en GitHub
2. Click en la pestaña "Actions"
3. Deberías ver el workflow ejecutándose
4. Si todo está verde ✓, el CI/CD está funcionando

---

## 📊 Paso 3: Agregar Badges al README

Editar `README.md` y agregar al inicio (después del título):

```markdown
![CI Pipeline](https://github.com/Grisel86/iris-classification-ml/workflows/CI%20Pipeline/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
```

Commit y push:

```bash
git add README.md
git commit -m "Add CI badges to README"
git push
```

---

## 🎯 Paso 4: Crear Ramas de Desarrollo

### 4.1 Estrategia de branching

```bash
# Crear rama de desarrollo
git checkout -b develop
git push -u origin develop

# Para features nuevos
git checkout -b feature/add-cross-validation
# ... hacer cambios ...
git add .
git commit -m "Add cross-validation to model training"
git push -u origin feature/add-cross-validation
```

### 4.2 Flujo de trabajo recomendado

1. **main** - código en producción, siempre estable
2. **develop** - integración continua
3. **feature/** - features nuevos
4. **fix/** - bug fixes

---

## 📝 Paso 5: Proteger la Rama Main

En GitHub:

1. Ir a Settings → Branches
2. Click en "Add rule"
3. Branch name pattern: `main`
4. Marcar:
   - ✓ Require a pull request before merging
   - ✓ Require status checks to pass before merging
   - ✓ Require branches to be up to date before merging
5. Seleccionar el check "CI Pipeline / test"
6. Click "Create"

Ahora **nadie puede pushear directo a main** sin que pasen los tests.

---

## 🚨 Paso 6: Ejemplo de Workflow Completo

### Escenario: Agregar un nuevo feature

```bash
# 1. Crear rama feature
git checkout develop
git pull
git checkout -b feature/add-logistic-regression

# 2. Hacer cambios
# ... editar config.yaml para agregar LogisticRegression ...
# ... agregar tests ...

# 3. Verificar localmente
python tests/test_preprocessing.py
python main.py

# 4. Commit
git add .
git commit -m "Add Logistic Regression as alternative model"

# 5. Push
git push -u origin feature/add-logistic-regression

# 6. Crear Pull Request en GitHub
# - IR a GitHub
# - Click "Compare & pull request"
# - Esperar que pasen los checks de CI
# - Si todo está verde, hacer merge a develop

# 7. Cuando develop esté estable, merge a main
```

---

## 📈 Paso 7: Ver Resultados en GitHub

Después de cada push, GitHub Actions ejecuta:

1. ✓ Instala dependencias
2. ✓ Ejecuta tests
3. ✓ Ejecuta pipeline completo
4. ✓ Valida Quality Gate
5. ✓ Reporta si pasó o falló

Ver en: `https://github.com/Grisel86/iris-classification-ml/actions`

---

## 🎓 Conceptos de CI/CD que Acabamos de Implementar

| Concepto | Qué significa | Por qué importa |
|----------|---------------|-----------------|
| **Continuous Integration** | Código se integra y testea automáticamente | Detecta errores temprano |
| **Automated Testing** | Tests corren en cada push | No hay riesgo de olvidar correr tests |
| **Quality Gates** | Pipeline falla si accuracy < 85% | Garantiza calidad mínima |
| **Branch Protection** | Main requiere PR + tests | Código en main siempre funciona |
| **Status Badges** | Badges muestran estado en README | Profesionalismo + transparencia |

---

## ✅ Checklist Final

Antes de enviar el link del repo en una aplicación laboral:

- [ ] README completo con badges
- [ ] CI/CD funcionando (checks verdes en Actions)
- [ ] Tests pasando
- [ ] Código bien documentado
- [ ] .gitignore correcto (no subir .pkl files pesados)
- [ ] requirements.txt actualizado
- [ ] Commits con mensajes descriptivos
- [ ] Branch protection activada

---

## 🎯 Próximos Pasos Opcionales

1. **Agregar más tests**
   - Tests para train.py
   - Tests para evaluate.py
   - Tests de integración

2. **Agregar notebooks de EDA**
   - Análisis exploratorio
   - Visualizaciones

3. **Dockerizar**
   - Crear Dockerfile
   - Docker Compose para desarrollo

4. **Desplegar API**
   - FastAPI para predictions
   - Deploy en Heroku/Render

5. **MLOps avanzado**
   - Integrar MLflow para tracking
   - Versionar datasets con DVC
   - Automatizar retraining

---

## 💡 Tips para Interview

Cuando muestres este proyecto en entrevistas:

1. **Empezá por el problema**: "Construí un clasificador de flores que demuestra arquitectura ML profesional"

2. **Destacá lo diferenciador**: "No es solo un notebook - tiene testing, CI/CD, y Quality Gates"

3. **Mostrá el flujo**: Abrir GitHub Actions y mostrar los checks pasando en tiempo real

4. **Conectá con tu background**: "Apliqué mi experiencia en QA automation para implementar tests automatizados y validaciones de pipeline"

5. **Hablá de próximos pasos**: Demuestra que sabés cómo escalar esto

---

¡Éxito con tu transición a Data Science! 🚀
