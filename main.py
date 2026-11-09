from fastapi import FastAPI
from models import TextRequest, load_translation_model, translate_text

app = FastAPI()

#carregamento
model = load_translation_model()

#rota 1
@app.get("/")
def status():
    return {"message": "OK!"}

#retorno do texto traduzido
@app.post("/translate")
def translate(data: TextRequest):
    translation = translate_text(model, data.prompt)
    return {"translation_text": translation}