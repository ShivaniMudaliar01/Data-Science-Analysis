import joblib
import os
import pandas as pd
from transformers import pipeline

# Load model and label encoder
model = joblib.load("models/triage_model.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

# Load Hugging Face model pipeline
hf_model_name = "google/flan-t5-base"
llm = pipeline("text2text-generation", model=hf_model_name)

def explain_prediction(input_df: pd.DataFrame):
    """
    Given a single patient data row (DataFrame with one row),
    returns:
      - predicted class label (Low/Medium/High)
      - None for SHAP (removed)
      - LLM text explanation using Hugging Face
    """
    # Predict probabilities and class
    pred_proba = model.predict_proba(input_df)[0]
    pred_class_idx = pred_proba.argmax()
    pred_class_label = label_encoder.inverse_transform([pred_class_idx])[0]

    # Build a human-readable summary of input features
    feature_summary = "\n".join(
        f"{col}: {val}" for col, val in input_df.iloc[0].items()
    )

    # Enhanced prompt for better LLM explanation
    prompt = f"""
You are a medical AI assistant.

A patient has the following vitals and symptoms:
{feature_summary}

The model has predicted the triage level as: {pred_class_label}.

Using common medical reasoning, explain whether this patient may be at HIGH, MEDIUM, or LOW risk, and provide a clear explanation in simple terms.

Keep in mind that severe symptoms like chest pain, high fever, fast heart rate, very low or high blood pressure, or difficulty breathing indicate HIGH risk.
Mild or normal vitals usually suggest LOW risk.
"""

    try:
        response = llm(prompt, max_new_tokens=150)[0]["generated_text"].strip()
    except Exception as e:
        response = f"LLM explanation failed: {e}"

    return pred_class_label, None, response
