import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

def classify_email(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    result = response.json()

    if not isinstance(result, list):
        return "Erro", "Não foi possível classificar o texto."

    label = result[0]['label']
    score = result[0]['score']

    if label == "POSITIVE":
        return "Produtivo", f"Confiança: {score:.2f}"
    else:
        return "Improdutivo", f"Confiança: {score:.2f}"
