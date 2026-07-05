"""
Module: Document Loader

Purpose:
    Loads PDF documents from the knowledge folder and converts each page
    into a LangChain Document object for further processing in the RAG pipeline.
"""



from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


class DocumentLoader:
    def __init__(self, knowledge_path: str):
        self.knowledge_path = Path(knowledge_path)

    def load_documents(self):
        documents = []

        pdf_files = list(self.knowledge_path.glob("*.pdf"))

        if not pdf_files:
            print("❌ No PDF files found.")
            return documents

        for pdf in pdf_files:
            print(f"📄 Loading: {pdf.name}")

            loader = PyPDFLoader(str(pdf))
            docs = loader.load()

            documents.extend(docs)

        print(f"\n✅ Total Pages Loaded: {len(documents)}")

        return documents