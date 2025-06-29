from . import db
from sqlalchemy.dialects.sqlite import JSON

class Sesion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_sesion = db.Column(db.String(10), unique=True, nullable=False)
    fecha = db.Column(db.String(20), nullable=False)
    tipo_dia = db.Column(db.String(20), nullable=False)
    duracion = db.Column(db.Integer, nullable=False)
    jugadores_disponibles = db.Column(JSON)
    modulos = db.Column(JSON)
    observaciones = db.Column(db.Text)