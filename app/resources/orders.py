from app.models.user import User
from flask_restful import Resource


class Orders(Resource):
    @staticmethod
    def get():
        return []


class OrdersByUser(Resource):
    @staticmethod
    def get(user_id):
        user = User.query.get(user_id)

        if user is None:
            return 'User not found', 400

        order_array = []
        for order in user.orders.all():
            order_array.append(order.dictionary())

        return order_array
