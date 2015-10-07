from app import db
from app.models import User, Request, Country, PostalCode, Company, Product, Comment, RequestProduct
from tests.testbase import TestBase


class TestDB(TestBase):

    def test_insert_countries(self):
        country = Country(country_code="IS",
                          country_name="Iceland")
        db.session.add(country)
        iceland = Country.query.get("IS")
        assert(iceland.country_name == country.country_name)
        assert(iceland.country_code == country.country_code)

        test_postal_code1 = PostalCode(postal_code="101",
                                       country=iceland)
        db.session.add(test_postal_code1)

        test_postal_code2 = PostalCode(postal_code="102",
                                       country=iceland)
        db.session.add(test_postal_code2)

        postal_codes = PostalCode.query.filter(Country.country_code == "IS").all()
        assert len(postal_codes) == 2

    def test_insert_companies(self):
        country = Country(country_code="IS",
                          country_name="Iceland")
        db.session.add(country)

        company = Company(name="Superhero",
                          email="contact@superhero.com",
                          phone_number="364-234384")
        db.session.add(company)
        new_company = Company.query.first()
        assert company.name == new_company.name

    def test_insert_products(self):
        country = Country(country_code="IS",
                          country_name="Iceland")
        db.session.add(country)

        company = Company(name="Superhero",
                          email="contact@superhero.com",
                          phone_number="364-234384")
        db.session.add(company)

        pizza_product = Product(name="Pizza",
                                description="Pepperoni with ham",
                                company=company)
        db.session.add(pizza_product)

        product = Product.query.first()
        assert pizza_product.name == product.name

    def test_create_user(self):
        user = User(email="test@gmail.com",
                    first_name="Luis",
                    last_name="F",
                    address="Somewhere",
                    phone_number="2389432")

        db.session.add(user)
        recent_user = User.query.filter(User.email == user.email).first()
        assert(user == recent_user)

        request = Request(message="Pizza please!",
                          user=user)

        db.session.add(request)

        comment = Comment(message="Fast please!",
                          request=request,
                          user_comment=True)

        db.session.add(comment)
        recent_user = User.query.filter(User.email == user.email).first()

        assert(recent_user.request.first().comment.first() == comment)

        country = Country(country_code="IS",
                          country_name="Iceland")
        db.session.add(country)

        company = Company(name="Superhero",
                          email="contact@superhero.com",
                          phone_number="364-234384")
        db.session.add(company)

        pizza_product = Product(name="Pizza",
                                description="Pepperoni with ham",
                                company=company)
        sushi_product = Product(name="Sushi",
                                description="Pepperoni with ham",
                                company=company)
        db.session.add(pizza_product)
        db.session.add(sushi_product)

        request_product1 = RequestProduct(product=pizza_product,
                                          request=request)
        request_product2 = RequestProduct(product=sushi_product,
                                          request=request)

        db.session.add(request_product1)
        db.session.add(request_product2)

        request_products = RequestProduct.query.filter(RequestProduct.request_id == Request.id).all()
        assert len(request_products) == 2
