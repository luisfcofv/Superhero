from app import db
from app.models.user import Request, Comment, User
from flask import request
from flask_restful import Resource


class Requests(Resource):
    @staticmethod
    def get():
        requests = Request.query.all()
        requests_array = []

        for user_request in requests:
            requests_array.append(user_request.dictionary())

        return requests_array


class SingleRequest(Resource):
    @staticmethod
    def get(request_id):
        user_request = Request.query.filter(Request.id == request_id).first()

        if user_request is None:
            return 'Request not found', 400

        return user_request.dictionary()

    @staticmethod
    def patch(request_id):
        user_request = Request.query.filter(Request.id == request_id).first()

        if user_request is None:
            return 'Request not found', 400

        user_request.update_request(request.json)
        db.session.add(user_request)
        return user_request.dictionary()


class RequestComment(Resource):
    @staticmethod
    def get(request_id):
        user_request = Request.query.filter(Request.id == request_id).first()

        if user_request is None:
            return 'Request not found', 400

        comments = user_request.comment.all()
        comments_array = []

        for comment in comments:
            comments_array.append(comment.dictionary())

        return comments_array

    @staticmethod
    def post(request_id):
        user_request = Request.query.filter(Request.id == request_id).first()

        if user_request is None:
            return 'Request not found', 400

        data = request.json

        if "owner_id" not in data:
            return 'owner_id not provided', 400

        user = User.query.get(data["owner_id"])

        if user is None:
            return 'Invalid owner_id', 400

        comment = Comment(request.json, user_request, user)
        db.session.add(comment)
        db.session.commit()
        return comment.dictionary()
