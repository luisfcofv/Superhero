from app import db


class PostalCode(db.Model):
    __tablename__ = 'postals'
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String, db.ForeignKey('countries.country_code'))
    postal_code = db.Column(db.String, index=True)

    def dictionary(self):
        return {
            "country_code": self.country_code,
            "postal_code": self.postal_code
        }

    def __str__(self):
        return self.dictionary().__str__()

    def __eq__(self, other):
        return self.dictionary().__str__() == other.dictionary().__str__()
