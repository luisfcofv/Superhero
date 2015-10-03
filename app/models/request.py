from app import db
from datetime import datetime
from app.models import Comment


class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    comment = db.relationship('Request', foreign_keys=Comment.request_id, backref='owner',
                              cascade="save-update, merge, delete", lazy='dynamic')
