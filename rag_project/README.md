# 🧠 RAG-based Question Answering from PDF  
*A lightweight Retrieval-Augmented Generation (RAG) project using open-source tools*

This project allows you to ask natural language questions about a PDF document. It combines document retrieval and local language models using only free and open-source libraries like `LangChain`, `FAISS`, and `Transformers`.

---

## 📂 Project Structure

rag_project/

├── main.py                        ← Entry point to run RAG

├── config.py                      ← Constants and configuration

├── loader.py                      ← Loads and splits documents

├── embedder.py                    ← Embeds and stores chunks using FAISS

├── qa_chain.py                    ← Builds and runs the RAG QA chain

├── data/
│   └── your_doc.pdf               ← Your input document(s)

├── faiss_index/                   ← Saved vector store

├── chat_history                   ← Stores chat history (Auto Generated)

└── requirements.txt               ← Python dependencies


---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ShivaniMudaliar01/Data-Science-Analysis/tree/679c7b8fc4fbb5714ac6dfe66d624a54e37987d3/rag_project
cd rag_project
```

### 2. Create Virtual Environment (Optional but Recommended)
```
python -m venv .venv
source .venv/bin/activate       # On Windows: .venv\Scripts\activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```

## 📄 Add Your Document

Place your PDF inside the documents/ folder and rename it to your_doc.pdf.
Or, update the filename in main.py accordingly.

## 🚀 Run the App
```
python main.py
```

## *If you want to change the PDF document*
(e.g., replace your_doc.pdf with a new file), you must delete the existing FAISS index to regenerate embeddings and avoid mismatched results.

### 🔄 Steps to Reset the Index:
1. Replace the document in the documents/ folder:
```
documents/your_doc.pdf   # ← Place new PDF here with the same name
```
2. Delete the existing FAISS index directory:
```
rm -rf faiss_index/       # On Linux/macOS

# OR

rmdir /s /q faiss_index   # On Windows CMD

```
3. Run the app again to reprocess the new document:
```
python main.py
```


### Example output:

🧠 Ask a question (or type 'exit'): What is Data Science?

💬 Answer: Data science is an interdisciplinary field that...

### 🛠️ How It Works

Document Loading: PDF is split into small chunks.

Embedding Generation: Each chunk is converted into embeddings using sentence-transformers.

Retrieval: Similar chunks are retrieved from the FAISS index.

Answer Generation: A local language model (flan-t5-base) generates an answer using the retrieved content.

## 🤖 Tech Stack

| Layer           | Tool Used                                |
| --------------- | ---------------------------------------- |
| Embeddings      | `sentence-transformers/all-MiniLM-L6-v2` |
| Retriever       | FAISS (`langchain.vectorstores.FAISS`)   |
| LLM             | `google/flan-t5-base` (via Transformers) |
| Document Loader | `PyPDF2` + LangChain splitters           |
| Orchestration   | `LangChain`                              |

## ✅ Example Use Cases
Question answering over technical documentation

Chatbot over company policies or product manuals

## 📃 Chat Log Format
All conversations are saved in chat_history.txt:

Lightweight RAG prototype for learning or demos

### 📚 References
LangChain Documentation

Hugging Face Transformers

FAISS (Facebook AI)



