from app import db
from app.models import User, Request, Comment
from tests.testbase import TestBase


class TestDB(TestBase):
    def test_create_user(self):
        user = User(email="test@gmail.com",
                    first_name="Luis",
                    last_name="F",
                    address="Somewhere",
                    phone_number="2389432")

        db.session.add(user)
        recent_user = User.query.filter(User.email == user.email).first()
        assert(user == recent_user)

        request = Request(title="I want donuts",
                          message="Dozen of donuts & 2 lts milk",
                          user=user)

        db.session.add(request)
        recent_user = User.query.filter(User.email == user.email).first()
        assert(recent_user.request.first() == request)

        comment = Comment(message="From Dunkin Donuts Please!",
                          user=user,
                          request=request)

        db.session.add(comment)
        recent_user = User.query.filter(User.email == user.email).first()

        assert(recent_user.request.first().comment.first() == comment)

