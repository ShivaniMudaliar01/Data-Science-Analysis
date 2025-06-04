# Patient Triage Data Generator & Predictor

This project simulates patient triage data and provides a simple machine learning model to predict triage severity levels based on patient vitals and symptoms. It also includes a Streamlit app for interactive exploration and prediction.

## Project Structure

- `app/create_data.py` — Script to generate dummy patient triage data and save as CSV.
- `app/predictor.py` — Script to train and save the triage prediction model.
- `app/ui.py` — Streamlit app to interactively predict triage levels using the trained model.
- `data/` — Folder where generated CSV data and model files are stored.

## Getting Started

1. Generate Dummy Data

Run the data creation script to generate simulated patient data:

```bash
python app/create_data.py

# Triage Prioritizer Project

This project simulates patient triage prioritization based on generated dummy health data.

```

## How to Use

- **Generate Data:**  
  Run `app.create_data.py` to generate dummy patient data and save it as a CSV file.

- **Create Model:**  
  Run `predictor.py` to train the triage prediction model using the generated data.

- **Run the App:**  
  Use Streamlit to launch the user interface with the command:  
  ```bash
  streamlit run app/ui.py
