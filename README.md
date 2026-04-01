# 🌸 Iris Flower Classification using Machine Learning

End-to-end **Machine Learning classification project** that predicts the species of an Iris flower  
(*Setosa, Versicolor or Virginica*) based on its morphological features.

This project demonstrates a complete **data science workflow**, including data loading,
preprocessing, model training, evaluation, testing, and prediction.

---

## 🚀 Project Overview

The Iris dataset is a classic benchmark in machine learning and statistics.  
It contains 150 samples with the following features:

- Sepal length
- Sepal width
- Petal length
- Petal width

The goal is to **build, train, and evaluate a supervised classification model** capable of
accurately predicting the flower species.

---

## 🧠 Machine Learning Workflow

1. Data loading and validation  
2. Data preprocessing and feature scaling  
3. Model training  
4. Model evaluation  
5. Prediction on new samples  
6. Unit testing  

The project is structured following **best practices used in real-world ML projects**.

---

## 📊 Model Performance & Metrics

The final model was evaluated using a hold-out test set.

**Evaluation metrics:**

- ✅ Accuracy: **≈ 96–98%**
- ✅ Precision: High for all classes
- ✅ Recall: High for all classes
- ✅ F1-score: Balanced across classes

Example classification report:
      precision    recall  f1-score   support
Setosa           1.00      1.00      1.00        10
Versicolor       0.93      0.90      0.92        10
Virginica        0.95      0.98      0.96        10
Accuracy                             0.96        30

> ✅ These results indicate strong generalization performance with minimal overfitting.

---

## 📁 Project Structure


iris-classification-project/
│
├── config/
│   └── config.yaml              # Project configuration
│
├── data/
│   ├── raw/                     # Raw input data (iris.csv)
│   └── processed/               # Processed datasets
│
├── notebooks/                   # Data exploration and analysis
│
├── src/
│   ├── data/                    # Data loading and preprocessing
│   ├── features/                # Feature engineering
│   ├── models/                  # Training and evaluation logic
│   └── utils/                   # Utility functions
│
├── tests/                       # Unit tests
│
├── main.py                      # Training pipeline
├── predict.py                   # Inference script
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
└── GITHUB_GUIDE.md              # Git & workflow guide

---

## ⚙️ Installation

1. Clone the repository:
git clone https://github.com/Grisel86/iris-classification-ml.git
cd iris-classification-project

Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

Install dependencies:
pip install -r requirements.txt

▶️ Usage
Train the model

python main.py

Run predictions
python predict.py

✅ Testing
Unit tests ensure data consistency and preprocessing correctness.

pytest tests/

🛠️ Technologies & Tools

Python 3
Pandas
NumPy
Scikit-learn
Pytest
Git & GitHub


🎯 Project Goals

Apply a full Machine Learning pipeline
Follow clean code and a modular project structure
Practice ML model evaluation and testing
Use Git/GitHub with professional workflows


💼 Why this project?
This project was developed as part of a professional portfolio to demonstrate:

Practical Machine Learning skills
Code organization aligned with industry standards
Ability to evaluate and document models clearly
Reproducible and maintainable ML pipelines


👩‍💻 Author
Fabiana Grisel Gonzalez
Machine Learning / Data Science Student
📍 Santa Cruz, Argentina
🔗 GitHub: https://github.com/Grisel86

