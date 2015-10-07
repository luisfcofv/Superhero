from app import db
from app.models import RequestProduct
from datetime import datetime


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    name = db.Column(db.String)
    description = db.Column(db.String)
    product_request = db.relationship('RequestProduct', foreign_keys=RequestProduct.product_id, backref='product',
                                      cascade="save-update, merge, delete", lazy='dynamic')

    def dictionary(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),
            "company_id": self.company_id,
            "name": self.name,
            "description": self.description
        }

    def __str__(self):
        return self.dictionary().__str__()
