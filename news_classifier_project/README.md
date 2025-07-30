# 🗞️ News Classifier Project

This project provides a simple **news classification and summarization API** using Hugging Face Transformers with optional dataset preparation and training. Built with FastAPI, it classifies news into categories like **sports**, **politics**, **technology**, and **entertainment**.

---

## 📁 Project Structure

news_classifier_project/

├── data/ #CREATE THE FOLDER

│ └── ag_news.csv # News dataset (downloaded via downloader.py)

├── models/

│ └── classifier.py # Classification model using Hugging Face

│ └── summarizer.py # Summarization model (can be LLM or RAG-based)

├── pipeline/

│ └── preprocess.py # Text preprocessing utilities

├── utils/

│ └── downloader.py # Script to download or scrape AG News dataset

├── app.py # FastAPI app with classification & summarization routes

├── app.log # Log file for incoming requests & predictions (Auto-Generated)

├── train.py # Script to train a custom classifier

└── requirements.txt # Project dependencies


---

## 🚀 Setup Instructions

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/ShivaniMudaliar01/Data-Science-Analysis/tree/001123414ed534357ec199a4a5426f7d39260c0c/news_classifier_project
cd news_classifier_project
```
### 2. Create and Activate a Virtual Environment

<strong>Windows</strong>
  
```
python -m venv .venv
.venv\Scripts\activate
```
### 3. Install Dependencies
   
```
pip install -r requirements.txt
```

### 4. Download Dataset

Run this script to populate the data/ directory with AG News or another dataset:
```
python utils/downloader.py
```
This will create:

data/

└── ag_news.csv

### 5. Run the FastAPI App
   
Use uvicorn to serve the API:
```
uvicorn app:app --reload
```
Expected log:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```
---

## 📬 API Endpoints

### 🔍 POST /classify

<b> Classifies news into one of the four categories ["technology", "entertainment", "sports", "politics"] </b>

Sample curl command:

#### 1. 🛰️ Technology News
```
curl -X POST http://127.0.0.1:8000/classify -H "Content-Type: application/json" -d "{\"text\": \"NASA announced a new mission to explore Mars by 2030.\"}"
```

Response:

{
  "labels": ["technology", "entertainment", "sports", "politics"],
  
  "scores": [0.74, 0.14, 0.06, 0.04],
  
  "top_label": "technology"
}

#### 2. 🎬 Entertainment News
```
curl -X POST http://127.0.0.1:8000/classify -H "Content-Type: application/json" -d "{\"text\": \"The new Avengers movie breaks box office records.\"}"
```
#### 3. 🏏 Sports News
```
curl -X POST http://127.0.0.1:8000/classify -H "Content-Type: application/json" -d "{\"text\": \"India wins T20 World Cup in a thrilling final match.\"}"
```

### 📝 POST /summarize

Generates a short summary of the input text.

Sample curl command:
```
curl -X POST http://127.0.0.1:8000/summarize -H "Content-Type: application/json" -d "{\"text\": \"NASA has revealed a new space exploration initiative focusing on Mars. The mission aims to...\"}"
```
Response:

{
  "summary": "NASA announced a new Mars exploration initiative."
}

---

## 🧪 Optional: Train a Custom Model

You can train your own news classifier using train.py. The script assumes preprocessed data and can be customized for your own pipeline.

```
python train.py
```
---

## 🪵 Logging

All classification and summarization requests are automatically logged in app.log with timestamped entries for traceability.






