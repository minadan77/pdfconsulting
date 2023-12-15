from flask import Flask, render_template, request
import spacy
from PyPDF2 import PdfFileReader

app = Flask(__name__)

# Carga del modelo de spaCy
nlp = spacy.load("es_core_news_sm")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/procesar_pdf", methods=["POST"])
def procesar_pdf():
    if request.method == "POST":
        # Procesamiento del archivo PDF
        pdf_file = request.files["pdf_file"]
        text = extraer_texto(pdf_file)
        
        # Procesamiento de lenguaje natural con spaCy
        doc = nlp(text)
        
        # Realizar aquí las operaciones deseadas con el documento spaCy (resumen, traducción, etc.)
        # Ejemplo: obtener entidades nombradas
        entidades = [ent.text for ent in doc.ents]

        return render_template("index.html", resultados=entidades)

def extraer_texto(pdf_file):
    # Extraer texto de un archivo PDF
    text = ""
    with open(pdf_file, "rb") as file:
        pdf_reader = PdfFileReader(file)
        for page_num in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page_num).extractText()
    return text

if __name__ == "__main__":
    app.run(debug=True)
