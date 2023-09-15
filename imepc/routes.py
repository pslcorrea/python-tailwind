from flask import render_template, url_for
from sqlalchemy import select

from imepc import app, database
from imepc.models import Media

@app.route("/")
def home():
    fotos = Media.query.filter_by(tipo='foto').order_by(Media.data.desc()).all()

    return render_template('index.html', fotos=fotos)

@app.route("/galeria")
def galeria():
   videos = Media.query.filter_by(tipo='video').order_by(Media.data.desc()).all()
   return render_template('galeria.html', videos=videos)

@app.route("/doacoes")
def doacores():
   return render_template('doacoes.html')