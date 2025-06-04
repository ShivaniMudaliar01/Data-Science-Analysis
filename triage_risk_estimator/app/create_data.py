import pandas as pd
import random
import os


def generate_dummy_data(n=250):
    data = []

    # Mapping severity to realistic symptoms
    symptoms_map = {
        'mild': ["Fatigue", "Headache"],
        'moderate': ["Fever", "Cough", "Nausea"],
        'severe': ["Chest Pain", "Shortness of Breath"]
    }

    for _ in range(n):
        age = random.randint(20, 80)
        bp = random.randint(100, 160)
        heart_rate = random.randint(60, 130)
        temp = round(random.uniform(36.0, 40.5), 1)
        resp_rate = random.randint(12, 30)

        severity_level = random.choices(['mild', 'moderate', 'severe'], weights=[0.4, 0.4, 0.2])[0]
        symptom = random.choice(symptoms_map[severity_level])

        # Triage logic for label
        if severity_level == 'severe' or bp > 150 or heart_rate > 110 or temp > 39.0:
            triage_label = 'High'
        elif severity_level == 'moderate':
            triage_label = 'Medium'
        else:
            triage_label = 'Low'

        data.append([
            age,
            heart_rate,
            bp,
            temp,
            resp_rate,
            symptom,
            triage_label
        ])

    df = pd.DataFrame(data, columns=[
        'age',
        'heart_rate',
        'blood_pressure',
        'temperature',
        'respiratory_rate',
        'symptom',
        'triage_level'
    ])
    return df


# Generate and save data
os.makedirs("data", exist_ok=True)
df = generate_dummy_data()
df.to_csv("data/patient_data.csv", index=False)
print("✅ Dummy triage data saved to data/patient_data.csv")
print(df.head())
