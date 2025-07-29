from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import config
import os

def get_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBED_MODEL)
    index_file = os.path.join(config.FAISS_DIR, "index.faiss")
    metadata_file = os.path.join(config.FAISS_DIR, "index.pkl")

    if os.path.exists(index_file) and os.path.exists(metadata_file):
        return FAISS.load_local(config.FAISS_DIR, embeddings, allow_dangerous_deserialization=True)

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(config.FAISS_DIR)
    return db

