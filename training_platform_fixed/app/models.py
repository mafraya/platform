from . import db

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    session_number = db.Column(db.Integer, unique=True)
    day_type = db.Column(db.String(20))
    moment = db.Column(db.String(50))
    submoment = db.Column(db.String(50))
    content = db.Column(db.String(100))
    players = db.Column(db.String(200))