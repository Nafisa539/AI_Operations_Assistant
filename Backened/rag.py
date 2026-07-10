import os
 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
 
# Folder paths
PDF_FOLDER = "../documents"
DB_FOLDER = "vector_db"
 
# Read all PDF files
documents = []
 
for file in os.listdir(PDF_FOLDER):
 
    if file.endswith(".pdf"):
 
        loader = PyPDFLoader(os.path.join(PDF_FOLDER, file))
        documents.extend(loader.load())
 
print("PDFs Loaded Successfully")
 
# Split the PDFs
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
 
chunks = text_splitter.split_documents(documents)
 
print("Chunks Created :", len(chunks))
 
# Create Embeddings
embedding = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)
 
print("Embeddings Created")
 
# Store in ChromaDB
db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory=DB_FOLDER
)
 
print("Vector Database Created")
 
# Search Function
def rag_search(question):
 
    result = db.similarity_search(question, k=1)
 
    if len(result) > 0:
        return result[0].page_content
 
    return None