# TP2 Parte 1 Questão 2 — Tradução com FastAPI

Neste exercício, a API recebe um texto em inglês e retorna a tradução para o francês.
Utilizei FastAPI e o modelo Helsinki-NLP/opus-mt-en-fr da Hugging Face.

## Arquivos

- `main.py`: inicia a aplicação e define as rotas.
- `models.py`: define a entrada, carrega o modelo e realiza a tradução.
- `teste_modelo.py`: testa frases curtas e um texto maior pelo terminal.
- `requirements.txt`: contém as bibliotecas utilizadas.

## Como executar

Com o Python instalado, abra o terminal dentro da pasta do projeto.

Crie o ambiente virtual: python -m venv .venv

Instalação das bibliotecas utilizadas: .\.venv\Scripts\python.exe -m pip install -r requirements.txt

Inicialização: .\.venv\Scripts\python.exe -m uvicorn main:app --port 8001

## Como testar

Acesse a rota inicial: http://127.0.0.1:8001/
Para gerar as traduções: http://127.0.0.1:8001/docs

Abra POST /translate, clique em Try it out, informe o JSON e clique em **Execute**:

{"prompt": "The cat is on the table."}
A resposta deve apresentar o código 200 e o campo `translation_text` com a tradução em francês.


## Sobre o uso de IA

Usei ChatGPT como apoio para ajudar na elaboração do código e conferencias.