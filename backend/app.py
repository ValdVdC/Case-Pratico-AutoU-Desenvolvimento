from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from classifier import classify_email
from responder import gerar_resposta
import os
import pdfplumber

app = Flask(__name__)
CORS(app)

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/classify', methods=['POST'])
def classify():
    text = ""
    file = request.files.get("file")
    input_text = request.form.get("text")

    if file:
        ext = os.path.splitext(file.filename)[1]
        if ext == ".pdf":
            text = extract_text_from_pdf(file)
        elif ext == ".txt":
            text = file.read().decode("utf-8")
    elif input_text:
        text = input_text
    else:
        return jsonify({"error": "Nenhum texto fornecido"}), 400

    categoria, confianca = classify_email(text)
    resposta = gerar_resposta(text, categoria)

    return jsonify({
        "categoria": categoria,
        "confianca": confianca,
        "resposta": resposta
    })

if __name__ == "__main__":
    app.run(debug=True)
