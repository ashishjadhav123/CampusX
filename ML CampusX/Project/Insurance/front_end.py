import streamlit as st
import joblib
import pandas as pd

model = joblib.load('insurance_model.pkl')

st.title("Insurance Charges Predictor 💸")

age = st.slider("Age", 18, 100)
bmi = st.slider("BMI", 10.0, 50.0)
children = st.slider("Children", 0, 5)
sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

input_df = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker],
    'region': [region]
})

if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Charges: ₹{prediction[0]:,.2f}")