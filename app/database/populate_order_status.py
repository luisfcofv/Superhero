from app import db
from app.models import OrderStatus


class PopulateOrderStatus:
    @staticmethod
    def insert_order_status():
        order_status = OrderStatus.query.all()

        if len(order_status) > 0:
            return

        order_status_received = OrderStatus(status="Order Received")
        db.session.add(order_status_received)

        order_status_preparation = OrderStatus(status="Preparation")
        db.session.add(order_status_preparation)

        order_status_delivery = OrderStatus(status="Out For Delivery")
        db.session.add(order_status_delivery)
