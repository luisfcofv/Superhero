from app import db
from app.models import Comment, RequestProduct
from datetime import datetime


class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    comment = db.relationship('Comment', foreign_keys=Comment.request_id, backref='request',
                              cascade="save-update, merge, delete", lazy='dynamic')
    product_request = db.relationship('RequestProduct', foreign_keys=RequestProduct.request_id, backref='request',
                                      cascade="save-update, merge, delete", lazy='dynamic')

    # def __init__(self, dictionary, user):
    #     self.user = user
    #     self.update_request(dictionary)

    def update_request(self, dictionary):
        self.message = dictionary["message"]

    def dictionary(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "message": self.message,
            "date": self.timestamp.isoformat()
        }

    def __str__(self):
        return self.dictionary().__str__()
