from app import db
from app.models import Product
from datetime import datetime


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    country_code = db.Column(db.String, db.ForeignKey('countries.country_code'))
    email = db.Column(db.String)
    name = db.Column(db.String)
    phone_number = db.Column(db.String)
    address = db.Column(db.String)
    product = db.relationship('Product', foreign_keys=Product.company_id, backref='product',
                              cascade="save-update, merge, delete", lazy='dynamic')
