from app import db
from app.models import Order, OrderStatus, OrderProduct, User
from flask import request
from flask_restful import Resource


class Orders(Resource):
    def get(self):
        return []


class OrdersByUser(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)

        if user is None:
            return 'User not found', 400

        order_array = []
        for order in user.orders.all():
            order_array.append(order.dictionary())

        return order_array

    def post(self, user_id):
        user = User.query.get(user_id)

        if user is None:
            return 'User not found', 400

        order_status = OrderStatus.query.first()

        print(order_status)

        order = Order(user=user, order_status=order_status)
        db.session.add(order)

        data = request.json
        for order_product_dict in data:
            order_product = OrderProduct(order=order,
                                         quantity=order_product_dict['quantity'],
                                         product_id=order_product_dict['product_id'])
            db.session.add(order_product)

        db.session.commit()
        return order.dictionary()
