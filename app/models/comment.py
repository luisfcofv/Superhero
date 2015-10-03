from app import db
from datetime import datetime


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    request_id = db.Column(db.Integer, db.ForeignKey('requests.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    message = db.Column(db.Text)

    def __str__(self):
        return self.message
