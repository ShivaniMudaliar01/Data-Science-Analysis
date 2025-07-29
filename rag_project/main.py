# main.py

from loader import load_and_split_document
from embedder import get_vectorstore
from qa_chain import get_rag_chain

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


def main():
    print("🔄 Loading and splitting document...")
    chunks = load_and_split_document()

    print("🔎 Creating or loading vectorstore...")
    vectorstore = get_vectorstore(chunks)

    print("🤖 Building RAG pipeline...")
    rag = get_rag_chain(vectorstore)

    while True:
        query = input("\n🧠 Ask a question (or type 'exit'): ")
        if query.lower() in ["exit", "quit"]:
            break
        answer = rag.invoke({"query": query})
        print(f"💬 Answer: {answer['result']}")

        # ✅ Save to chat history
        with open("chat_history.txt", "a", encoding="utf-8") as f:
            f.write(f"Q: {query}\nA: {answer['result']}\n\n")

if __name__ == "__main__":
    main()
