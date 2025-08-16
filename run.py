from flask import Flask
from app.controllers.rag_controller import api as rag_namespace
from flask_restx import Api

app = Flask(__name__)
api = Api(app, version='1.0', title='API RAG',
    description='Uma API para perguntas e respostas baseada em documentos.',
)

api.add_namespace(rag_namespace, path='/rag')

if __name__ == '__main__':
    app.run(debug=True)

