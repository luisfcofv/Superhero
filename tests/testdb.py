from app import db
from app.models import User, Order, Country, PostalCode, Company, Product, CompanyPostalCode, OrderProduct
from tests.testbase import TestBase


class TestDB(TestBase):

    def test_insert_countries(self):
        country = Country(country_code="IS", country_name="Iceland")
        db.session.add(country)
        iceland = Country.query.get("IS")
        assert iceland.country_name == country.country_name
        assert iceland.country_code == country.country_code

        test_postal_code1 = PostalCode(postal_code="101", country=iceland)
        test_postal_code2 = PostalCode(postal_code="102", country=iceland)

        db.session.add(test_postal_code1)
        db.session.add(test_postal_code2)

        postal_codes = PostalCode.query.filter(PostalCode.country_code == "IS").all()
        assert len(postal_codes) == 2

    def test_insert_companies(self):
        country = Country(country_code="IS",
                          country_name="Iceland")
        db.session.add(country)
        iceland = Country.query.get("IS")
        company = Company(name="Superhero",
                          email="contact@superhero.com",
                          phone_number="364-234384",
                          country=iceland)

        db.session.add(company)
        new_company = Company.query.first()
        assert company.name == new_company.name
        assert company.country_code == country.country_code

    def test_insert_company_postal_codes(self):
        iceland = Country(country_code="IS", country_name="Iceland")
        db.session.add(iceland)

        test_postal_code1 = PostalCode(postal_code="101", country=iceland)
        test_postal_code2 = PostalCode(postal_code="102", country=iceland)
        test_postal_code3 = PostalCode(postal_code="103", country=iceland)

        db.session.add(test_postal_code1)
        db.session.add(test_postal_code2)
        db.session.add(test_postal_code3)

        postal_codes = PostalCode.query.filter(Country.country_code == "IS").all()
        assert len(postal_codes) == 3

        company = Company(name="Superhero",
                          email="contact@superhero.com",
                          phone_number="364-234384",
                          country=iceland)
        db.session.add(company)

        pizza_product = Product(name="Pizza", description="Pepperoni with ham", company=company)
        sushi_product = Product(name="Sushi", description="Pepperoni with ham", company=company)
        db.session.add(pizza_product)
        db.session.add(sushi_product)

        company_postal_code1 = CompanyPostalCode(company=company, postal_code=test_postal_code1)
        company_postal_code2 = CompanyPostalCode(company=company, postal_code=test_postal_code3)

        db.session.add(company_postal_code1)
        db.session.add(company_postal_code2)

        company_postal_codes = CompanyPostalCode.query.all()
        assert len(company_postal_codes) == 2

        another_company = Company(name="Taqueria",
                                  email="contact@superhero.com",
                                  phone_number="364-234384",
                                  country=iceland)
        db.session.add(another_company)

        tacos_product = Product(name="Tacos", description="Yummi", company=another_company)
        db.session.add(tacos_product)

        company_postal_code3 = CompanyPostalCode(company=another_company, postal_code=test_postal_code2)
        company_postal_code4 = CompanyPostalCode(company=another_company, postal_code=test_postal_code3)

        db.session.add(company_postal_code3)
        db.session.add(company_postal_code4)

        # Search IS 101
        postal_code = PostalCode.query.filter(PostalCode.country_code == "IS", PostalCode.postal_code == "101").first()
        company_postal_codes = CompanyPostalCode.query.filter(CompanyPostalCode.postal_code_id == postal_code.id).all()

        cont = 0
        for company_postal_code in company_postal_codes:
            company = Company.query.filter(Company.id == company_postal_code.company_id).first()
            cont += len(company.products.all())

        assert cont == 2

        # Search IS 102
        postal_code = PostalCode.query.filter(PostalCode.country_code == "IS", PostalCode.postal_code == "102").first()
        company_postal_codes = CompanyPostalCode.query.filter(CompanyPostalCode.postal_code_id == postal_code.id).all()

        cont = 0
        for company_postal_code in company_postal_codes:
            company = Company.query.filter(Company.id == company_postal_code.company_id).first()
            cont += len(company.products.all())

        assert cont == 1

        # Search IS 103
        postal_code = PostalCode.query.filter(PostalCode.country_code == "IS", PostalCode.postal_code == "103").first()
        company_postal_codes = CompanyPostalCode.query.filter(CompanyPostalCode.postal_code_id == postal_code.id).all()

        cont = 0
        for company_postal_code in company_postal_codes:
            company = Company.query.filter(Company.id == company_postal_code.company_id).first()
            cont += len(company.products.all())

        assert cont == 3

    def test_insert_products(self):
        country = Country(country_code="IS", country_name="Iceland")
        db.session.add(country)

        company = Company(name="Superhero", email="contact@superhero.com", phone_number="364-234384")
        db.session.add(company)

        pizza_product = Product(name="Pizza", description="Pepperoni with ham", company=company)
        db.session.add(pizza_product)

        product = Product.query.first()
        assert pizza_product.name == product.name

    def test_insert_user(self):
        user = User(email="test@gmail.com",
                    first_name="Luis",
                    last_name="F",
                    address="Somewhere",
                    phone_number="2389432")

        db.session.add(user)
        recent_user = User.query.filter(User.email == user.email).first()
        assert user == recent_user

    def test_insert_orders(self):
        user = User(email="test@gmail.com",
                    first_name="Luis",
                    last_name="F",
                    address="Somewhere",
                    phone_number="2389432")
        db.session.add(user)

        iceland = Country(country_code="IS", country_name="Iceland")
        db.session.add(iceland)

        company = Company(name="Superhero",
                          email="contact@superhero.com",
                          phone_number="364-234384",
                          country=iceland)

        pizza_product = Product(name="Pizza", description="Pepperoni with ham", company=company)
        sushi_product = Product(name="Sushi", description="Sushi", company=company)
        db.session.add(pizza_product)
        db.session.add(sushi_product)

        order = Order(user=user)
        db.session.add(order)

        order_product1 = OrderProduct(product=pizza_product, order=order, quantity=2)
        order_product2 = OrderProduct(product=sushi_product, order=order, quantity=1)

        db.session.add(order_product1)
        db.session.add(order_product2)

        recent_user = user.query.get(1)

        assert len(recent_user.orders.all()) == 1
        assert len(recent_user.orders.first().order_products.all()) == 2
