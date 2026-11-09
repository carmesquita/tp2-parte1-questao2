from transformers import pipeline
from pydantic import BaseModel


#Modelo dos dados recebidos pela API
class TextRequest(BaseModel):
    prompt: str

#função para carregar o modelo de tradução
def load_translation_model():
    model = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr", device="cpu")
    return model

#tradução do texto
def translate_text(model, text):
    predictions = model(text)
    return predictions[0]["translation_text"]