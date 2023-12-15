import bard

app = bard.App()

def query(pdf):
  response = app.query(pdf)
  return response

if __name__ == "__main__":
  app.run()
