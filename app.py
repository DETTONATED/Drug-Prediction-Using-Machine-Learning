import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("drug_model.pkl")

st.set_page_config(
    page_title="Drug Prediction System",
    page_icon="💊",
    layout="centered"
)

st.title("💊 Drug Prediction System")
st.markdown("Predict the most suitable drug based on patient attributes.")

age = st.slider("Age", 15, 80, 30)

sex = st.selectbox(
    "Sex",
    ["F", "M"]
)

bp = st.selectbox(
    "Blood Pressure",
    ["HIGH", "LOW", "NORMAL"]
)

cholesterol = st.selectbox(
    "Cholesterol",
    ["HIGH", "NORMAL"]
)

na_to_k = st.number_input(
    "Na_to_K Ratio",
    min_value=0.0,
    value=10.0
)

sex_map = {
    "F": 0,
    "M": 1
}

bp_map = {
    "HIGH": 0,
    "LOW": 1,
    "NORMAL": 2
}

chol_map = {
    "HIGH": 0,
    "NORMAL": 1
}

if st.button("Predict Drug"):

    data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex_map[sex]],
        "BP": [bp_map[bp]],
        "Cholesterol": [chol_map[cholesterol]],
        "Na_to_K": [na_to_k]
    })

    prediction = model.predict(data)[0]

    st.success(f"Recommended Drug : {prediction}")