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




