from imepc import database
from flask_login import UserMixin
from datetime import datetime

class Usuario(database.Model, UserMixin):
  id = database.Column(database.Integer, primary_key=True)
  name = database.Column(database.String, nullable=False)
  email = database.Column(database.String, nullable=False)
  senha = database.Column(database.String, nullable=False)

class  Media(database.Model):
  id = database.Column(database.Integer, primary_key=True)
  titulo = database.Column(database.String, nullable=False)
  subtitulo = database.Column(database.String, nullable=True)
  comentario = database.Column(database.String, nullable=True)
  data = database.Column(database.Date, nullable=True, default=datetime.utcnow())
  link = database.Column(database.String, nullable=False)
  tipo = database.Column(database.String, nullable=False)

class Text(database.Model):
  id = database.Column(database.Integer, primary_key=True)
  classificacao = database.Column(database.String, nullable=True)
  texto = database.Column(database.String, nullable=False)