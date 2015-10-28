from app import db


class OrderProduct(db.Model):
    __tablename__ = 'order_products'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer)

    def dictionary(self):
        return {
            "product_id": self.product_id,
            "quantity": self.quantity
        }

    def __str__(self):
        return self.dictionary().__str__()
