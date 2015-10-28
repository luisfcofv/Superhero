from app import db
from app.models import Company, Country, PostalCode, Product, CompanyPostalCode, User, Order, OrderProduct


class PopulateFake:

    @staticmethod
    def insert_data():
        user = User.query.get(1)

        if user is not None:
            # Already populated
            return

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

        mexico = Country(country_code="MX", country_name="Mexico")
        db.session.add(mexico)

        postal_code_db = PostalCode(postal_code="101", country=mexico)
        db.session.add(postal_code_db)

        mexican_company = Company(name="Taqueria en Mexico",
                                  address="Calle 2",
                                  email="contact@mexico.com",
                                  phone_number="364-123456",
                                  thumbnail="http://www.taqueriadf.com/images/logo.gif",
                                  country=mexico)
        db.session.add(mexican_company)

        user = User(email="test@gmail.com",
                    first_name="Luis",
                    last_name="F",
                    address="Somewhere",
                    phone_number="2389432")
        db.session.add(user)

        order = Order(user=user)
        db.session.add(order)

        order_product1 = OrderProduct(product=pizza_product, order=order, quantity=2)
        order_product2 = OrderProduct(product=sushi_product, order=order, quantity=1)

        db.session.add(order_product1)
        db.session.add(order_product2)

