from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

import config

def get_rag_chain(vectorstore):
    qa_pipeline = pipeline(
        "text2text-generation",  # flan-t5 uses text2text-generation
        model=config.LLM_MODEL,
        max_length=256,
        temperature=0
    )
    llm = HuggingFacePipeline(pipeline=qa_pipeline)

    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        chain_type="stuff"
    )
    return rag_chain
