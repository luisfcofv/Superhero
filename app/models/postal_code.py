from app import db
from app.models import Company


class PostalCode(db.Model):
    __tablename__ = 'postal_codes'
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String, db.ForeignKey('countries.country_code'))
    postal_code = db.Column(db.String, index=True)
    company = db.relationship('Company', foreign_keys=Company.id, backref='postal_code',
                              cascade="save-update, merge, delete", lazy='dynamic')

    def dictionary(self):
        return {
            "country_code": self.country_code,
            "postal_code": self.postal_code
        }

    def __str__(self):
        return self.dictionary().__str__()

    def __eq__(self, other):
        return self.dictionary().__str__() == other.dictionary().__str__()
