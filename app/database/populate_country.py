from app import db
from app.models import Country, PostalCode


class PopulateCountry:
    @staticmethod
    def insert_countries():
        PopulateCountry.insert_iceland()

    @staticmethod
    def insert_iceland():
        iceland = Country.query.get("IS")

        if iceland is not None:
            return

        iceland = Country(country_code="IS", country_name="Iceland")
        db.session.add(iceland)

        for postal_code in range(101, 113 + 1):
            postal_code_db = PostalCode(postal_code=str(postal_code), country=iceland)
            db.session.add(postal_code_db)
