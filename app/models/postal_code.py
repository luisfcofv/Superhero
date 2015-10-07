from app import db


class PostalCodes(db.Model):
    __tablename__ = 'postals'
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer)
    postal_code = db.Column(db.String)
