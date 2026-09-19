# 🧪 Vaccine Usage Prediction using Machine Learning

## 📌 Project Overview
This project applies machine learning techniques to predict whether individuals are likely to take the **H1N1 vaccine** based on survey data.  
The goal is to help public health agencies identify hesitant groups and design targeted awareness campaigns.

---

## 📂 Dataset
- **Source**: H1N1 Vaccine Survey (CDC / Kaggle)
- **Features**: Demographics, health behaviors, opinions about vaccines, and social factors
- **Target Variable**: `h1n1_vaccine` (binary: 0 = No, 1 = Yes)
- **Format**: CSV

---

## ⚙️ Methodology
1. **Data Preprocessing**
   - Handle missing values
   - Encode categorical variables
   - Scale numerical features

2. **Model Training**
   - Logistic Regression (baseline)
   - Random Forest Classifier
   - XGBoost Classifier

3. **Evaluation Metrics**
   - Accuracy
   - Precision, Recall, F1-score
   - ROC-AUC
   - Confusion Matrix

---

## 📊 Results
- Logistic Regression: Provided a strong baseline
- Random Forest: Balanced performance across metrics
- XGBoost: Achieved the best recall and ROC-AUC, making it most effective for identifying vaccine adopters

---

## 📈 Visualizations
- Confusion Matrix Heatmaps
- ROC Curves
- Feature Importance (Random Forest / XGBoost)

---

## ✅ Conclusion
Machine learning models can effectively predict vaccine usage behavior.  
Among the tested models, **XGBoost performed best**, offering valuable insights for public health strategies to improve vaccine adoption.

---


