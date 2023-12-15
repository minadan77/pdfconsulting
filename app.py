import transformers

app = Flask(__name__)

model = transformers.T5ForConditionalGeneration.from_pretrained("t5-base")

@app.route("/upload")
def upload():
  pdf = request.files["pdf"]

  pdf_content = pdf.read()

  response = model.generate(input_text=pdf_content)

  question = response[0]["input_text"]
  answer = response[0]["output_text"]

  return render_template("index.html", question=question, answer=answer)

if __name__ == "__main__":
  app.run()
