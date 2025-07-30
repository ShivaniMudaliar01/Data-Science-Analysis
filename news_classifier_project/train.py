from models.classifier import NewsClassifier
from datasets import load_dataset
from pipeline.preprocess import preprocess
import torch

model = NewsClassifier()
dataset = load_dataset("ag_news")['train']
optimizer = torch.optim.Adam(model.parameters(), lr=2e-5)

for item in dataset.select(range(500)):
    inputs = preprocess(item['text'])
    labels = torch.tensor([item['label']])
    outputs = model(**inputs)
    loss = torch.nn.CrossEntropyLoss()(outputs.logits, labels)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()

torch.save(model.state_dict(), "news_classifier.pt")
