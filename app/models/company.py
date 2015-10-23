from app import db
from app.models import Product, CompanyPostalCode
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
    thumbnail = db.Column(db.String)
    products = db.relationship('Product', foreign_keys=Product.company_id, backref='company',
                               cascade="save-update, merge, delete", lazy='dynamic')
    company_postal_code = db.relationship('CompanyPostalCode', foreign_keys=CompanyPostalCode.company_id,
                                          backref='company', cascade="save-update, merge, delete", lazy='dynamic')

    def dictionary(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "logo_url": self.thumbnail,
            "phone_number": self.phone_number,
            "address": self.address,
            "country_code": self.country_code
        }

    def __str__(self):
        return self.dictionary().__str__()

