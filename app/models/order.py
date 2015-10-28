from app import db
from app.models import OrderProduct
from datetime import datetime


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    order_products = db.relationship('OrderProduct', foreign_keys=OrderProduct.order_id,
                                     backref='order', cascade="save-update, merge, delete", lazy='dynamic')

    def dictionary(self):

        dict = []
        for order_product in self.order_products.all():
            dict.append(order_product.dictionary())

        return {
            "id": self.id,
            "user_id": self.user_id,
            "date": self.timestamp.isoformat(),
            "order_products": dict
        }

    def __str__(self):
        return self.dictionary().__str__()