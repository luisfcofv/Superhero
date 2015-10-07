from app import db
from app.models import Request
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone_number = db.Column(db.String)
    address = db.Column(db.String)
    request = db.relationship('Request', foreign_keys=Request.user_id, backref='user',
                              cascade="save-update, merge, delete", lazy='dynamic')

    # def __init__(self, dictionary):
    #     self.id = dictionary["id"]
    #     self.update_user(dictionary)

    def update_user(self, dictionary):
        if "email" in dictionary:
            self.email = dictionary["email"]

        if "first_name" in dictionary:
            self.first_name = dictionary["first_name"]

        if "last_name" in dictionary:
            self.last_name = dictionary["last_name"]

        if "address" in dictionary:
            self.address = dictionary["address"]

        if "phone_number" in dictionary:
            self.phone_number = dictionary["phone_number"]

    def dictionary(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "phone_number": self.phone_number,
        }

    def __str__(self):
        return self.email

    def __eq__(self, other):
        return self.email == other.email
