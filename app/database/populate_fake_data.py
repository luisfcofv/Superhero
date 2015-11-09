from app import db
from app.models import Company, Country, PostalCode, Product, CompanyPostalCode, User, Order, OrderStatus, OrderProduct


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
                          email="info@superhero.xyz",
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
                                  email="info@taqueria.com",
                                  phone_number="364-123456",
                                  thumbnail="http://www.taqueriadf.com/images/logo.gif",
                                  country=iceland)
        db.session.add(another_company)

        tacos_product = Product(name="Tacos", description="Real tacos!", company=another_company, price="750.50")
        db.session.add(tacos_product)

        company_postal_code3 = CompanyPostalCode(company=another_company, postal_code=postal_code_101)
        db.session.add(company_postal_code3)

        pizza_rvk = Company(name="Pizza Reykjavik",
                            address="Borgartún 8",
                            email="info@pizza.com",
                            phone_number="364-123456",
                            thumbnail="http://previews.123rf.com/images/glorcza/glorcza1111/glorcza111100012/11273011-pizza-logo-Stock-Vector-restaurant.jpg",
                            country=iceland)
        db.session.add(pizza_rvk)

        company_postal_code4 = CompanyPostalCode(company=pizza_rvk, postal_code=postal_code_101)
        db.session.add(company_postal_code4)

        company_postal_code5 = CompanyPostalCode(company=pizza_rvk, postal_code=postal_code_102)
        db.session.add(company_postal_code5)

        hamburgers_rvk = Company(name="Hamburgers Reykjavik",
                                 address="Midtún 8",
                                 email="info@hamburgers.com",
                                 phone_number="364-16533",
                                 thumbnail="http://www.clker.com/cliparts/4/e/7/d/12456867691315417792gramzon_Hamburger.svg.hi.png",
                                 country=iceland)
        db.session.add(hamburgers_rvk)

        company_postal_code6 = CompanyPostalCode(company=hamburgers_rvk, postal_code=postal_code_101)
        db.session.add(company_postal_code6)

        company_postal_code7 = CompanyPostalCode(company=hamburgers_rvk, postal_code=postal_code_102)
        db.session.add(company_postal_code7)

        sushi_rvk = Company(name="Sushi Reykjavik",
                            address="Tún 1",
                            email="info@sushi.com",
                            phone_number="364-71243",
                            thumbnail="http://www.soultravelmultimedia.com/wp-content/uploads/2011/11/Sushi-Logo-11.png",
                            country=iceland)
        db.session.add(sushi_rvk)

        company_postal_code8 = CompanyPostalCode(company=sushi_rvk, postal_code=postal_code_101)
        db.session.add(company_postal_code8)

        company_postal_code9 = CompanyPostalCode(company=sushi_rvk, postal_code=postal_code_102)
        db.session.add(company_postal_code9)

        user = User(email="test@gmail.com",
                    first_name="Luis",
                    last_name="F",
                    address="Somewhere",
                    phone_number="2389432")
        db.session.add(user)

        order_status = OrderStatus.query.first()
        order = Order(user=user, order_status=order_status)

        db.session.add(order)

        order_product1 = OrderProduct(product=pizza_product, order=order, quantity=2)
        order_product2 = OrderProduct(product=sushi_product, order=order, quantity=1)

        db.session.add(order_product1)
        db.session.add(order_product2)

