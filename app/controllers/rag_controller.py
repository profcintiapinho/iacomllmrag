import os
from flask import Blueprint, request
from flask_restx import Namespace, Resource, fields
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from app.models.rag_model import RAGModel

# Configurações do RAG
DOC_DIR = "documents"
DB_DIR = "db"

# Cria um namespace para a API
api = Namespace('rag', description='API para consultas RAG')

# Modelo de entrada para a API
rag_question = api.model('Question', {
    'question': fields.String(required=True, description='A pergunta para o sistema RAG.')
})

# Cria o modelo de embeddings
model_name = "BAAI/bge-small-en"
embedding_function = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    encode_kwargs={'normalize_embeddings': True}
)

# Instancia o modelo RAG
rag_model = RAGModel(db_path=DB_DIR, embedding_function=embedding_function)

@api.route('/ask')
class RAGAsk(Resource):
    @api.expect(rag_question)
    def post(self):
        """
        Faz uma pergunta ao sistema RAG e obtém uma resposta com base nos documentos.
        """
        data = request.json
        question = data.get('question')

        if not question:
            return {'error': 'A pergunta é obrigatória.'}, 400

        try:
            response = rag_model.get_rag_response(question)
            return {"response": response}
        except Exception as e:
            return {'error': str(e)}, 500