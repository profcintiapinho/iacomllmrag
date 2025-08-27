# Para testar esse projeto em sua máquina
### Esse projeto já foi testado com python versões: 3.11 e 3.13, no 3.14 ele não roda por conta da versão do chroma que não foi compatível

## Baixe e instale de acordo com seu sistema (Windows, Linux ou Mac).

Verifique se está funcionando:

* ollama --version

## Se for, por exemplo, llama3, rode:

* ollama pull llama3

## Clonar o repositório do projeto (Direto no vscode)

https://github.com/profcintiapinho/iacomllmrag.git

## Criar e ativar um ambiente virtual Python no terminal(prompt), não esqueça que precisar estar na pasta onde fez o clone

* python -m venv venv

* venv/bin/activate   

* venv\Scripts\activate

## Instalar as dependências

* pip install -r requirements.txt

<img width="639" height="445" alt="image" src="https://github.com/user-attachments/assets/61e153f8-72d6-4a96-a28e-5f0567292d4c" />

## Configurar o banco de dados / embeddings

python setup_database.py

Sempre que você trocar os documentos de consulta, precisa executar esses códigos novamente:

<img width="962" height="520" alt="image" src="https://github.com/user-attachments/assets/b6631cee-8531-4c28-a820-6be9287bae12" />

## Entenda a estrutura de pastas

IACOMLLMRAG/
│
├── app/                     → pasta principal da aplicação
│   ├── __pycache__/          → arquivos compilados automaticamente pelo Python
│   │   └── __init__.cpython-313.pyc
│   ├── controllers/          → camada de controle (regras de execução e lógica)
│   │   ├── __pycache__/
│   │   └── rag_controller.py → controla a lógica do RAG (faz ligação entre modelo, dados e views)
│   ├── models/               → camada de dados/modelos
│   │   ├── __pycache__/
│   │   └── rag_model.py      → define como os dados/documentos são tratados e usados pelo RAG
│   └── views/                → camada de apresentação (retorno ao usuário, interface API ou CLI)
│       ├── __init__.py       → indica que a pasta é um módulo Python
│       └── __init__.py       → (parece duplicado, mas serve para inicializar pacote)
│
├── db/                       → banco de dados vetorial do ChromaDB
│   ├── e4495eaa-b2d8...      → pasta interna criada pelo ChromaDB com metadados
│   └── chroma.sqlite3        → banco SQLite onde ficam embeddings/documentos indexados
│
├── documents/                → documentos de referência para o RAG
│   ├── arquivosquedevemserconsultados.pdf → fonte de conhecimento em PDF
│   └── problemas.csv         → dados estruturados (ex.: perguntas/respostas ou base de teste)
│
├── venv/                     → ambiente virtual Python (dependências instaladas só aqui)
│
├── .gitignore                → lista de arquivos/pastas ignorados pelo Git (ex.: venv, pycache, db local)
├── README.md                 → instruções principais do projeto (como rodar, dependências, etc.)
├── requirements.txt          → dependências necessárias (bibliotecas Python com versão)
├── run.py                    → script principal que inicia a aplicação (carrega modelos e roda)
└── setup_database.py         → script que prepara o banco/ChromaDB (gera embeddings e popula o db)




