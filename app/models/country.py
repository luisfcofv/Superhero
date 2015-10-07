from app import db
from app.models import Company, PostalCode


class Country(db.Model):
    __tablename__ = 'countries'
    country_code = db.Column(db.String, primary_key=True)
    country_name = db.Column(db.String)
    company = db.relationship('Company', foreign_keys=Company.country_code, backref='country',
                              cascade="save-update, merge, delete", lazy='dynamic')
    postal_code = db.relationship('PostalCode', foreign_keys=PostalCode.country_code, backref='country',
                                  cascade="save-update, merge, delete", lazy='dynamic')

    def dictionary(self):
        return {
            "country_code": self.country_code,
            "country_name": self.country_name
        }

    def __str__(self):
        return self.dictionary().__str__()
