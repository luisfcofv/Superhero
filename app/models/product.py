from app import db
from app.models import OrderProduct
from datetime import datetime


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Float)
    order_product = db.relationship('OrderProduct', foreign_keys=OrderProduct.product_id, backref='product',
                                    cascade="save-update, merge, delete", lazy='dynamic')

    def dictionary(self):
        return {
            "id": self.id,
            "company_id": self.company_id,
            "name": self.name,
            "description": self.description,
            "price": self.price
        }

    def __str__(self):
        return self.dictionary().__str__()
