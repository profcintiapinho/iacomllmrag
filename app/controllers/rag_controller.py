import os
from flask import request
from flask_restx import Namespace, Resource, fields

# Importa config centralizada
from app.config import get_embedding_function
from app.models.rag_model import RAGModel

# Caminhos
DOC_DIR = "documents"
DB_DIR = "db"

# Cria um namespace para a API
api = Namespace('rag', description='API para consultas RAG')

# Modelo de entrada da API
rag_question = api.model('Question', {
    'question': fields.String(required=True, description='A pergunta para o sistema RAG.')
})

# Cria embeddings a partir do config centralizado
embedding_function = get_embedding_function()

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