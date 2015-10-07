from app import db
from datetime import datetime


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('requests.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    message = db.Column(db.Text)
    user_comment = db.Column(db.Boolean)

    def __init__(self, dictionary, request, user):
        self.request = request
        self.user = user
        self.update_comment(dictionary)

    def update_comment(self, dictionary):
        self.message = dictionary["message"]

    def dictionary(self):
        return {
            "id": self.id,
            "user_id": self.owner_id,
            "request_id": self.request_id,
            "message": self.message,
            "date": self.timestamp.isoformat()
        }

    def __str__(self):
        return self.message
