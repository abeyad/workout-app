# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Welcome to Hamza & Ali's workout app!</h1>"

if __name__ == '__main__':
  app.run()
