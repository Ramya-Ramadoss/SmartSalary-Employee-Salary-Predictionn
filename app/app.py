import streamlit as st
import pandas as pd
import joblib
import os

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="SmartSalary",
    page_icon="💼",
    layout="centered"
)

# =========================
# LOAD MODEL
# =========================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "salary_model.pkl"
)

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error(f"Error Loading Model: {e}")
    st.stop()

# =========================
# TITLE
# =========================

st.title("💼 SmartSalary")
st.subheader("Employee Salary Prediction System")

st.write(
    "Predict employee salary using Machine Learning."
)

# =========================
# USER INPUTS
# =========================

experience_years = st.number_input(
    "Experience Years",
    min_value=0,
    max_value=50,
    value=5
)

skills_count = st.number_input(
    "Skills Count",
    min_value=0,
    max_value=50,
    value=5
)

certifications = st.selectbox(
    "Certifications",
    [0, 1]
)

job_title = st.selectbox(
    "Job Title",
    [
        "Backend Developer",
        "Business Analyst",
        "Cloud Engineer",
        "Cybersecurity Analyst",
        "Data Analyst",
        "Data Scientist",
        "DevOps Engineer",
        "Frontend Developer",
        "Machine Learning Engineer",
        "Product Manager",
        "Software Engineer"
    ]
)

education_level = st.selectbox(
    "Education Level",
    [
        "Diploma",
        "High School",
        "Master",
        "PhD"
    ]
)

industry = st.selectbox(
    "Industry",
    [
        "Education",
        "Finance",
        "Government",
        "Healthcare",
        "Manufacturing",
        "Media",
        "Retail",
        "Technology",
        "Telecom"
    ]
)

company_size = st.selectbox(
    "Company Size",
    [
        "Large",
        "Medium",
        "Small",
        "Startup"
    ]
)

location = st.selectbox(
    "Location",
    [
        "Canada",
        "Germany",
        "India",
        "Netherlands",
        "Remote",
        "Singapore",
        "Sweden",
        "UK",
        "USA"
    ]
)

remote_work = st.selectbox(
    "Remote Work",
    [
        "No",
        "Yes"
    ]
)

# =========================
# PREDICTION
# =========================

if st.button("Predict Salary"):

    columns = [
        "experience_years",
        "skills_count",
        "certifications",
        "job_title_Backend Developer",
        "job_title_Business Analyst",
        "job_title_Cloud Engineer",
        "job_title_Cybersecurity Analyst",
        "job_title_Data Analyst",
        "job_title_Data Scientist",
        "job_title_DevOps Engineer",
        "job_title_Frontend Developer",
        "job_title_Machine Learning Engineer",
        "job_title_Product Manager",
        "job_title_Software Engineer",
        "education_level_Diploma",
        "education_level_High School",
        "education_level_Master",
        "education_level_PhD",
        "industry_Education",
        "industry_Finance",
        "industry_Government",
        "industry_Healthcare",
        "industry_Manufacturing",
        "industry_Media",
        "industry_Retail",
        "industry_Technology",
        "industry_Telecom",
        "company_size_Large",
        "company_size_Medium",
        "company_size_Small",
        "company_size_Startup",
        "location_Canada",
        "location_Germany",
        "location_India",
        "location_Netherlands",
        "location_Remote",
        "location_Singapore",
        "location_Sweden",
        "location_UK",
        "location_USA",
        "remote_work_No",
        "remote_work_Yes"
    ]

    input_data = pd.DataFrame(
        [[0] * len(columns)],
        columns=columns
    )

    # Numerical Features
    input_data["experience_years"] = experience_years
    input_data["skills_count"] = skills_count
    input_data["certifications"] = certifications

    # One-Hot Encoded Features
    input_data[f"job_title_{job_title}"] = 1
    input_data[f"education_level_{education_level}"] = 1
    input_data[f"industry_{industry}"] = 1
    input_data[f"company_size_{company_size}"] = 1
    input_data[f"location_{location}"] = 1
    input_data[f"remote_work_{remote_work}"] = 1

    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted Salary: ${prediction:,.2f}"
    )

    st.metric(
        label="Estimated Salary",
        value=f"${prediction:,.2f}"
    )