import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from predictor import model
from explain import explain_prediction
from lime import lime_tabular
import sys
import os

# Optional: suppress torch file watcher warnings (Windows users)
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Define triage label mapping
triage_labels = {0: "Low", 1: "Medium", 2: "High"}

# UI Setup
st.set_page_config(page_title="Triage Risk Score Estimator", layout="centered")
st.title("🚑 Triage Prioritizer")
st.markdown("""
This tool helps assess patient urgency based on vitals and symptoms. 
Predictions are made using a trained XGBoost model with LIME-based explainability.
""")

with st.form("triage_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Age", 20, 90, 40)
        heart_rate = st.slider("Heart Rate (bpm)", 50, 140, 80)
        bp = st.slider("Blood Pressure (mmHg)", 90, 180, 120)
    with col2:
        temp = st.slider("Temperature (°F)", 95.0, 105.0, 98.6)
        resp_rate = st.slider("Respiratory Rate (breaths/min)", 10, 35, 16)
        symptom = st.selectbox("Symptom", ['Headache', 'Fever', 'Cough', 'Chest Pain', 'Shortness of Breath'])

    submitted = st.form_submit_button("Predict Urgency")

if submitted:
    # Create input DataFrame
    input_df = pd.DataFrame([{
        "age": age,
        "heart_rate": heart_rate,
        "blood_pressure": bp,
        "temperature": temp,
        "respiratory_rate": resp_rate,
        "symptom": symptom
    }])

    # One-hot encode symptom to match training format
    input_df = pd.get_dummies(input_df)

    # Align columns with model input
    model_input_cols = model.get_booster().feature_names
    for col in model_input_cols:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[model_input_cols]

    # Make prediction
    pred_idx = int(model.predict(input_df)[0])  # 0, 1, or 2
    pred_label = triage_labels[pred_idx]

    # Load training data for LIME explanation
    train_df = pd.read_csv("data/patient_data.csv")  # Adjust path if needed
    train_df = pd.get_dummies(train_df)
    for col in model_input_cols:
        if col not in train_df.columns:
            train_df[col] = 0
    train_df = train_df[model_input_cols]

    # LIME explainer setup
    explainer = lime_tabular.LimeTabularExplainer(
        training_data=train_df.values,
        feature_names=train_df.columns.tolist(),
        class_names=list(triage_labels.values()),
        mode='classification'
    )

    exp = explainer.explain_instance(
        data_row=input_df.values[0],
        predict_fn=model.predict_proba,
        num_features=6
    )

    # Results display
    st.subheader("🔍 Prediction")
    st.success(f"Predicted Triage Level: **{pred_label}**")

    st.subheader("📊 LIME Explanation")
    fig = exp.as_pyplot_figure()
    st.pyplot(fig)

    st.subheader("🧠 LLM-based Reasoning")
    _, _, explanation = explain_prediction(input_df)
    st.markdown(f"> {explanation}")
