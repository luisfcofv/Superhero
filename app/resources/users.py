from app import db
from app.models.user import User
from flask import request
from flask_restful import Resource


class Users(Resource):
    @staticmethod
    def get():
        users = User.query.all()
        users_array = []

        for user in users:
            users_array.append(user.dictionary())

        return users_array

    @staticmethod
    def post():
        data = request.json

        if "id" not in data or data["id"] is None:
            return 'Id not provided', 400

        new_user = User(data)
        user = User.query.filter(User.id == new_user.id).first()

        if user is None:
            db.session.add(new_user)
            db.session.commit()
            return new_user.dictionary()
        else:
            return user.dictionary()


class SingleUser(Resource):
    @staticmethod
    def get(user_id):
        user = User.query.filter(User.id == user_id).first()

        if user is None:
            return 'User not found', 400

        return user.dictionary()

    @staticmethod
    def patch(user_id):
        user = User.query.filter(User.id == user_id).first()

        if user is None:
            return 'User not found', 400

        user.update_user(request.json)
        db.session.add(user)
        return user.dictionary()
