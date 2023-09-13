from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/galeria")
def galeria():
   return render_template('galeria.html')

@app.route("/doacoes")
def doacores():
   return render_template('doacoes.html')

if __name__== "__main__":
  app.run(debug=True)