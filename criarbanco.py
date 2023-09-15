from imepc import database, app
from imepc.models import Usuario, Media, Text

with app.app_context():
  database.create_all()