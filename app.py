import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("vaccine_model.pkl")

st.title("Vaccine Usage Prediction")

age = st.number_input("Age", 0, 100, 25)
income = st.number_input("Income", 0, 1000000, 50000)

if st.button("Predict"):
    data = pd.DataFrame({
        "Age":[age],
        "Income":[income]
    })

    prediction = model.predict(data)

    st.success(f"Prediction: {prediction[0]}")