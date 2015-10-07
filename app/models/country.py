from app import db


class Country(db.Model):
    __tablename__ = 'countries'
    country_code = db.Column(db.String, primary_key=True)
    country_name = db.Column(db.String)