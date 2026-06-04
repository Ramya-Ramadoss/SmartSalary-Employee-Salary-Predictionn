# SmartSalary: Employee Salary Prediction and Workforce Analytics

A machine learning project for predicting employee salary based on features such as experience, education, and job role.

## Project Overview

SmartSalary is a machine learning project that predicts employee salaries using workforce and job-related attributes. The project demonstrates a complete machine learning workflow, including data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, and feature importance analysis.

The objective is to understand the factors that influence employee compensation and build a predictive model capable of estimating salaries accurately.

---

## Problem Statement

Employee compensation depends on multiple factors such as professional experience, education level, job role, company size, certifications, industry, and location.

This project aims to predict employee salaries using machine learning techniques and identify the most influential factors affecting compensation.

This is a supervised machine learning regression problem.

---

## Dataset

The dataset contains employee and job-related information including:

* Job Title
* Experience Years
* Education Level
* Skills Count
* Industry
* Company Size
* Location
* Remote Work
* Certifications
* Salary (Target Variable)

Target Variable:

* Salary

---

## Project Workflow

### 1. Data Loading

* Imported dataset using Pandas
* Examined dataset structure and data types

### 2. Data Cleaning

* Checked missing values
* Removed duplicates
* Prepared data for analysis

### 3. Exploratory Data Analysis (EDA)

Performed analysis on:

* Salary Distribution
* Experience vs Salary
* Education vs Salary
* Industry vs Salary
* Company Size vs Salary
* Remote Work vs Salary

### 4. Feature Engineering

* Applied One-Hot Encoding
* Converted categorical features into numerical representations

### 5. Model Training

Models evaluated:

* Linear Regression
* Random Forest Regressor

### 6. Model Evaluation

Evaluation metrics:

* RMSE (Root Mean Squared Error)
* R² Score

---

## Model Performance

| Model                   | RMSE    | R² Score |
| ----------------------- | ------- | -------- |
| Random Forest Regressor | 7375.76 | 0.9609   |

The Random Forest model achieved excellent predictive performance, explaining approximately 96% of salary variation.

---

## Feature Importance Analysis

The most influential features identified by the model include:

* Experience Years
* Location (India, USA, Canada)
* Education Level (PhD)
* Company Size
* Job Title

These findings suggest that experience, geography, education, and organizational factors significantly impact employee compensation.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Jupyter Notebook
* Git
* GitHub

---

## Project Structure

```text
SmartSalary-Employee-Salary-Prediction

├── data
├── models
├── notebooks
├── reports
├── src
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Key Skills Demonstrated

* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* Machine Learning
* Regression Modeling
* Model Evaluation
* Feature Importance Analysis
* Git and GitHub

---

## Future Improvements

* Implement XGBoost and LightGBM
* Deploy using Streamlit
* Add interactive salary prediction dashboard
* Introduce salary recommendation features
* Perform advanced hyperparameter tuning

---

## Author

Ramya Ramadoss

B.Tech Computer Science and Engineering

Interested in Data Analytics, Machine Learning, Business Intelligence, and AI-driven decision systems.
