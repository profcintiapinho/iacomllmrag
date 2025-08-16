import os
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class RAGModel:
    def __init__(self, db_path, embedding_function):
        # Cria a conexão com o banco de dados vetorial
        self.vectorstore = Chroma(
            persist_directory=db_path,
            embedding_function=embedding_function
        )
        self.retriever = self.vectorstore.as_retriever()
        
        # Define o modelo de linguagem (LLM) que será usado para gerar a resposta
        self.llm = Ollama(model="llama3")

    def get_rag_response(self, question):
        # 1. Recupera os documentos relevantes (contexto)
        retrieved_docs = self.retriever.get_relevant_documents(question)
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])
        
        # 2. Cria o prompt aprimorado
        # Instruímos o modelo a usar apenas o contexto fornecido e a ser direto
        template = """
        Você é um assistente de IA. Responda a pergunta do usuário com base **exclusivamente** no seguinte contexto.
        Se a resposta não estiver no contexto, diga "Não encontrei essa informação nos documentos.".
        
        Contexto:
        {context}
        
        Pergunta:
        {question}
        
        Resposta:
        """
        
        prompt = ChatPromptTemplate.from_template(template)
        output_parser = StrOutputParser()
        
        # 3. Cria a cadeia de processamento (Chain)
        chain = prompt | self.llm | output_parser
        
        # 4. Verifica se o contexto está vazio para evitar respostas genéricas
        if not context.strip():
            return "Não encontrei informações relevantes para sua pergunta nos documentos."
            
        # 5. Executa a cadeia e retorna a resposta
        return chain.invoke({"context": context, "question": question})
