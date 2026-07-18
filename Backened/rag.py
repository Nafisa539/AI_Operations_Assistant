import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
 
# ------------------------------------
# Project Paths
# ------------------------------------
 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
 
pdf_folder = os.path.join(PROJECT_DIR, "documents")
db_folder = os.path.join(BASE_DIR, "chroma_db")
 
# ------------------------------------
# Embedding Model
# ------------------------------------
 
embedding = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)
 
# ------------------------------------
# Create / Load Vector Database
# ------------------------------------
 
if not os.path.exists(db_folder):
 
    documents = []
 
    if not os.path.exists(pdf_folder):
        raise FileNotFoundError(f"Documents folder not found: {pdf_folder}")
 
    for file in os.listdir(pdf_folder):
 
        if file.endswith(".pdf"):
 
            loader = PyPDFLoader(os.path.join(pdf_folder, file))
            documents.extend(loader.load())
 
    splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=30
)
 
    docs = splitter.split_documents(documents)
 
    db = Chroma.from_documents(
        docs,
        embedding,
        persist_directory=db_folder
    )
 
    db.persist()
 
else:
 
    db = Chroma(
        persist_directory=db_folder,
        embedding_function=embedding
    )
 
# ------------------------------------
# RAG Search Function
# ------------------------------------
 
def rag_search(question):
 
    keywords = question.lower().split()
 
    try:
        results = db.similarity_search(
            question,
            k=5
        )
    except Exception:
        return None
 
    paragraphs = []
 
    for doc in results:
 
        text = doc.page_content.strip()
 
        blocks = text.split("\n\n")
 
        for block in blocks:
 
            block = block.strip()
 
            if len(block) < 40:
                continue
 
            block_lower = block.lower()
 
            if any(word in block_lower for word in keywords):
 
                if block not in paragraphs:
                    paragraphs.append(block)
 
    if len(paragraphs) == 0:
 
        for doc in results:
 
            text = doc.page_content.strip()
 
            if text not in paragraphs:
                paragraphs.append(text)
 
    if len(paragraphs) == 0:
        return None
 
    return "\n\n".join(paragraphs[:3])