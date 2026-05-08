# Customer Churn Prediction System

A professional Machine Learning web application built using Python and Streamlit to predict whether a customer is likely to churn or stay.

---

##  Project Overview

This project helps businesses identify customers who are at risk of leaving their service.

Using customer-related features such as:

* tenure
* monthly charges
* support calls
* contract type
* internet service

the model predicts customer churn probability and provides business insights for retention strategies.

---

##  Features

*  Login & Register Authentication System
*  Interactive Dashboard
*  Real-Time Churn Prediction
*  Business Insights & Visualizations
*  Churn Probability & Risk Analysis
*  Professional Streamlit UI
*  Machine Learning Pipeline Integration

---

##  Machine Learning Workflow

### Models Tested

* Logistic Regression
* Random Forest Classifier
* CatBoost Classifier  (Best Model)

### Best Model

CatBoostClassifier

### Best Parameters

* Depth = 6
* Iterations = 200
* Learning Rate = 0.03

### Best Cross Validation Accuracy

84.84%

---

##  Techniques Used

* Pipeline
* ColumnTransformer
* GridSearchCV
* Cross Validation (cv=5)
* OneHotEncoding
* Feature Scaling
* Missing Value Imputation

---

##  Dataset Features

### Numerical Features

* monthly_charges
* total_charges
* tenure
* support_calls

### Categorical Features

* contract
* payment_method
* tech_support
* online_security
* internet_service

### Target Variable

`churn`

* 0 = Customer stays
* 1 = Customer leaves

---

## Key Business Insights

* Customers with month-to-month contracts churn more
* High support calls strongly increase churn risk
* New customers are more likely to leave
* Long-term customers are more stable

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* CatBoost
* Streamlit
* Matplotlib
* Seaborn

---

##  Project Structure

project/
│
├── app.py
├── churn_model.pkl
├── custome.csv
├── users.pkl
├── requirements.txt
└── README.md

---

##  How to Run

### 1️Install Requirements

pip install -r requirements.txt

### 2️ Run Streamlit App

streamlit run app.py

---

##  Future Improvements

* Cloud Deployment
* Advanced Interactive Charts
* Customer Retention Suggestions
* AI-Based Recommendation System
* Email Alerts for High-Risk Customers

---

##  Developed By

Yuvraj Mahajan

Machine Learning & Data Science Project
