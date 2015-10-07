from app import db
from app.models import Persona


class Company(Persona):
    __tablename__ = 'companies'
    name = db.Column(db.String)
    phone_number = db.Column(db.String)
    address = db.Column(db.String)
