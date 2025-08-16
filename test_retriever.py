import os
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

DB_PATH = "db"

print("Verificando se o banco de dados existe...")
if not os.path.exists(DB_PATH):
    print(f"Erro: A pasta '{DB_PATH}' não foi encontrada. Certifique-se de ter executado o script 'setup_database.py'.")
else:
    print("Pasta 'db' encontrada.")

    try:
        print("Carregando o modelo de embeddings...")
        embeddings = OllamaEmbeddings(model="llama3")

        print("Carregando o banco de dados vetorial...")
        db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
        print("Banco de dados carregado com sucesso!")

        print("Executando uma busca no banco de dados...")
        retriever = db.as_retriever()
        query = "Minha geladeira quebrou"
        retrieved_docs = retriever.invoke(query)

        print(f"Busca concluída. Documentos encontrados: {len(retrieved_docs)}")
        for doc in retrieved_docs:
            print("---")
            print(doc.page_content[:200] + "...") # Imprime as 200 primeiras letras

        print("\nTeste do retriever concluído com sucesso!")

    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao testar o retriever: {e}")
        import traceback
        traceback.print_exc()