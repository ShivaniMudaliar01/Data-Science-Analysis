from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def preprocess(text, max_len=256):
    return tokenizer(text, padding="max_length", truncation=True, max_length=max_len, return_tensors="pt")