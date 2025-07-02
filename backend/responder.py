import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

def gerar_resposta(email, categoria):
    prompt = f"Leia o seguinte email:\n\"{email}\"\n\nGere uma resposta {('objetiva e útil' if categoria == 'Produtivo' else 'educada e cordial, sem ação necessária')}."
    
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 100}}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    result = response.json()

    if isinstance(result, dict) and 'error' in result:
        return "Não foi possível gerar resposta."
    
    return result[0]['generated_text']
