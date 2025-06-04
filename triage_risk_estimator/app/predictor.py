import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

MODEL_PATH = "models/triage_model.pkl"
LABEL_PATH = "models/label_encoder.pkl"

def train_model():
    # Load data
    df = pd.read_csv("data/patient_data.csv")

    # Encode categorical column: 'symptom'
    df = pd.get_dummies(df, columns=['symptom'])

    # Label encode the target variable
    le = LabelEncoder()
    y = le.fit_transform(df['triage_level'])

    # Drop original target from features
    X = df.drop("triage_level", axis=1)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

    # Train model
    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
    model.fit(X_train, y_train)

    # Save model and encoder
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(le, LABEL_PATH)

    print("✅ Model and label encoder saved successfully.")

def load_model():
    model = joblib.load(MODEL_PATH)
    le = joblib.load(LABEL_PATH)
    return model, le

# Train if not already trained
if not os.path.exists(MODEL_PATH):
    train_model()

# Load for inference
model, label_encoder = load_model()
