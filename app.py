import bard

app = bard.App()

def query(pdf):
  response = app.query(pdf)
  if response.question:
    return response
  else:
    return None
