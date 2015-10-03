from app import db
from app.models import Request, Comment
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    signup_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone_number = db.Column(db.String)
    address = db.Column(db.String)
    request = db.relationship('Request', foreign_keys=Request.owner_id, backref='user',
                              cascade="save-update, merge, delete", lazy='dynamic')
    comment = db.relationship('Comment', foreign_keys=Comment.owner_id, backref='user',
                              cascade="save-update, merge, delete", lazy='dynamic')

    def __str__(self):
        return self.email

    def __eq__(self, other):
        return self.email == other.email