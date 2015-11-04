from app import db
from app.models import Order


class OrderStatus(db.Model):
    __tablename__ = 'order_status'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Text)
    order = db.relationship('Order', foreign_keys=Order.order_status_id, backref='order_status',
                            cascade="save-update, merge, delete", lazy='dynamic')

    def dictionary(self):
        return {
            "order_status_id": self.id,
            "status": self.status
        }

    def __str__(self):
        return self.dictionary().__str__()
