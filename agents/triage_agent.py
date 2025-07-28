import os
import json
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

class TriageAgent:
    def __init__(self, threat_db_path="data/threat_intel.json"):
        self.db = self.load_vector_db(threat_db_path)
        self.llm = OpenAI(temperature=0.3)

    def load_vector_db(self, path):
        with open(path) as f:
            data = json.load(f)

        documents = [
            Document(
                page_content=item["description"],
                metadata={"severity": item["severity"]}
            ) for item in data
        ]

        embedding = OpenAIEmbeddings()
        vectordb = Chroma.from_documents(documents, embedding, collection_name="threats")
        return vectordb

    def analyze_threat(self, threat_log):
        results = self.db.similarity_search(threat_log, k=2)

        context = "\n".join([doc.page_content for doc in results])
        prompt = f"""Given the following known threat descriptions:

{context}

Assess the severity of this log message: "{threat_log}"

Respond with a severity level (Low, Medium, High) and a brief reason."""

        response = self.llm.invoke(prompt)
        return response

