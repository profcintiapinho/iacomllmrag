import os
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
import shutil

# Pasta dos documentos estão localizados 
DOC_DIR = "documents"

# Caminho onde o banco de dados vetorial será armazenado
DB_DIR = "db"

# Remove o banco de dados anterior para começar do zero
if os.path.exists(DB_DIR):
    shutil.rmtree(DB_DIR)

documents = []
for file_name in os.listdir(DOC_DIR):
    file_path = os.path.join(DOC_DIR, file_name)
    if file_name.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
        documents.extend(loader.load())
    else:
        loader = TextLoader(file_path, encoding="utf-8")
        documents.extend(loader.load())

# Divide os documentos em chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

print(f"Total de documentos carregados: {len(documents)}")
print(f"Total de chunks criados: {len(docs)}")

# Cria o modelo de embeddings (vetorização)
print("Criando embeddings com o modelo 'all-MiniLM-L6-v2'...")
model_name = "BAAI/bge-small-en"
embedding_function = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    encode_kwargs={'normalize_embeddings': True}
)

# Cria o banco de dados vetorial
print("Armazenando no banco de dados vetorial...")
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_function,
    persist_directory=DB_DIR
)
print("Banco de dados vetorial criado e armazenado com sucesso.")