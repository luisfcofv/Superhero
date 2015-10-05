from app import db
from app.models.user import User, Request
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

        if "id" not in data:
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


class UserRequest(Resource):
    @staticmethod
    def get(user_id):
        user = User.query.filter(User.id == user_id).first()

        if user is None:
            return 'User not found', 400

        user_requests = user.request.all()
        requests_array = []

        for user_request in user_requests:
            requests_array.append(user_request.dictionary())

        return requests_array

    @staticmethod
    def post(user_id):
        user = User.query.filter(User.id == user_id).first()

        if user is None:
            return 'User not found', 400

        data = request.json
        new_request = Request(data, user)

        db.session.add(new_request)
        db.session.commit()
        return new_request.dictionary()
