from app import db
from app.models.user import User
from flask import request
from flask_restful import Resource


class Users(Resource):
    def get(self):
        """
        List all users
        ---
        tags:
          - Users
        definitions:
          - schema:
              id: User
              properties:
                id:
                 type: integer
                 description: the user's id
                email:
                 type: string
                 description: the user's email
                first_name:
                 type: string
                 description: the user's first name
                last_name:
                 type: string
                 description: the user's last name
                address:
                 type: string
                 description: the user's address
                phone_number:
                 type: string
                 description: the user's phone number

        responses:
          200:
            description: Lists all users
            schema:
                title: Users
                type: array
                items:
                    $ref: '#/definitions/User'
        """
        users = User.query.all()
        users_array = []

        for user in users:
            users_array.append(user.dictionary())

        return users_array

    def post(self):
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
    def get(self, user_id):
        user = User.query.filter(User.id == user_id).first()

        if user is None:
            return 'User not found', 400

        return user.dictionary()

    def patch(self, user_id):
        user = User.query.filter(User.id == user_id).first()

        if user is None:
            return 'User not found', 400

        user.update_user(request.json)
        db.session.add(user)
        return user.dictionary()
