from app import db
from app.models import Comment
from datetime import datetime


class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.Text)
    message = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    comment = db.relationship('Comment', foreign_keys=Comment.request_id, backref='request',
                              cascade="save-update, merge, delete", lazy='dynamic')

    def __init__(self, dictionary, user):
        self.user = user
        self.update_request(dictionary)

    def update_request(self, dictionary):
        self.title = dictionary["title"]
        self.message = dictionary["message"]

    def dictionary(self):
        return {
            "id": self.id,
            "user_id": self.owner_id,
            "title": self.title,
            "message": self.message,
            "date": self.timestamp.isoformat()
        }

    def __str__(self):
        return self.title
