from app import db
from datetime import datetime


class Persona(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    email = db.Column(db.String)
