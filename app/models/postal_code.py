from app import db
from app.models import CompanyPostalCode


class PostalCode(db.Model):
    __tablename__ = 'postal_codes'
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String, db.ForeignKey('countries.country_code'))
    postal_code = db.Column(db.String, index=True)
    company_postal_code = db.relationship('CompanyPostalCode', foreign_keys=CompanyPostalCode.postal_code_id,
                                          backref='postal_code', cascade="save-update, merge, delete", lazy='dynamic')

    def dictionary(self):
        return {
            "id": self.id,
            "country_code": self.country_code,
            "postal_code": self.postal_code
        }

    def __str__(self):
        return self.dictionary().__str__()

    def __eq__(self, other):
        return self.dictionary().__str__() == other.dictionary().__str__()
