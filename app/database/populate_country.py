from app import db
from app.models import Company, Country, PostalCode, Product, CompanyPostalCode


class PopulateCountry:
    @staticmethod
    def insert_countries():
        PopulateCountry.insert_iceland()
        PopulateCountry.mockup_insert_iceland()

    @staticmethod
    def insert_iceland():
        iceland = Country.query.get("IS")

        if iceland is None:
            iceland = Country(country_code="IS", country_name="Iceland")
            db.session.add(iceland)

        for postal_code in range(101, 113 + 1):
            postal_code_db = PostalCode.query.filter(PostalCode.country_code == "IS",
                                                     PostalCode.postal_code == str(postal_code)).first()
            if postal_code_db is None:
                postal_code_db = PostalCode(postal_code=str(postal_code), country=iceland)
                db.session.add(postal_code_db)

    @staticmethod
    def mockup_insert_iceland():
        iceland = Country.query.get("IS")

        postal_code_101 = PostalCode.query.filter(PostalCode.country_code == "IS",
                                                  PostalCode.postal_code == "101").first()

        postal_code_102 = PostalCode.query.filter(PostalCode.country_code == "IS",
                                                  PostalCode.postal_code == "102").first()

        company = Company(name="Superhero Restaurant",
                          address="Laugavegur 1",
                          email="contact@superhero.xyz",
                          phone_number="364-234384",
                          thumbnail="http://www.lexingtoncolony.com/wp-content/uploads/2014/07/dinner-thumbnail.png",
                          country=iceland)
        db.session.add(company)

        pizza_product = Product(name="Pizza", description="Pizza with pepperoni and ham", company=company, price="10.0")
        sushi_product = Product(name="Sushi", description="Wonderful sushi", company=company, price="200.0",)
        db.session.add(pizza_product)
        db.session.add(sushi_product)

        company_postal_code1 = CompanyPostalCode(company=company, postal_code=postal_code_101)
        company_postal_code2 = CompanyPostalCode(company=company, postal_code=postal_code_102)

        db.session.add(company_postal_code1)
        db.session.add(company_postal_code2)

        another_company = Company(name="Taqueria",
                                  address="Laugavegur 2",
                                  email="contact@taqueria.com",
                                  phone_number="364-123456",
                                  thumbnail="http://www.taqueriadf.com/images/logo.gif",
                                  country=iceland)
        db.session.add(another_company)

        tacos_product = Product(name="Tacos", description="Real tacos!", company=another_company, price="750.50")
        db.session.add(tacos_product)

        company_postal_code3 = CompanyPostalCode(company=another_company, postal_code=postal_code_101)

        db.session.add(company_postal_code3)

        mexico = Country.query.get("MX")

        if mexico is None:
            mexico = Country(country_code="MX", country_name="Mexico")
            db.session.add(mexico)

        postal_code_db = PostalCode.query.filter(PostalCode.country_code == "MX",
                                                 PostalCode.postal_code == "101").first()
        if postal_code_db is None:
            postal_code_db = PostalCode(postal_code="101", country=mexico)
            db.session.add(postal_code_db)

        mexican_company = Company(name="Taqueria en Mexico",
                                  address="Calle 2",
                                  email="contact@mexico.com",
                                  phone_number="364-123456",
                                  thumbnail="http://www.taqueriadf.com/images/logo.gif",
                                  country=mexico)
        db.session.add(mexican_company)
