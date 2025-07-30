from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline
import logging

# --------------------
# Configure Logging
# --------------------
logging.basicConfig(
    filename="app.log",                     # Log file name
    level=logging.INFO,                     # Set log level
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# --------------------
# Initialize FastAPI app
# --------------------
app = FastAPI()

# Initialize zero-shot classifier
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define possible categories
CANDIDATE_LABELS = ["sports", "politics", "technology", "entertainment"]

# Define request schema
class NewsRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    logger.info("GET / - Root endpoint hit")
    return {"message": "Welcome to the News Classifier API!"}

@app.post("/classify")
def classify_news(request: NewsRequest):
    logger.info(f"POST /classify - Received text: {request.text}")
    result = classifier(request.text, candidate_labels=CANDIDATE_LABELS)
    output = {
        "labels": result["labels"],
        "scores": result["scores"],
        "top_label": result["labels"][0]
    }
    logger.info(f"POST /classify - Result: {output}")
    return output

# Summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.post("/summarize")
def summarize_news(request: NewsRequest):
    logger.info(f"POST /summarize - Received text: {request.text}")
    summary = summarizer(request.text, max_length=60, min_length=20, do_sample=False)
    result = {"summary": summary[0]["summary_text"]}
    logger.info(f"POST /summarize - Summary: {result}")
    return result
