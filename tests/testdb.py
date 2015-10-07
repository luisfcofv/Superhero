from app import db
from app.models import User, Request, Country, PostalCode
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

    def test_create_user(self):
        user = User(email="test@gmail.com",
                    first_name="Luis",
                    last_name="F",
                    address="Somewhere",
                    phone_number="2389432")

        db.session.add(user)
        recent_user = User.query.filter(User.email == user.email).first()
        assert(user == recent_user)

        request = Request(title="I want donuts",
                          message="Dozen of donuts & 2 lts milk",
                          user=user)

        db.session.add(request)
        recent_user = User.query.filter(User.email == user.email).first()
        assert(recent_user.request.first() == request)

        # comment = Comment(message="From Dunkin Donuts Please!",
        #                   request=request)
        #
        # db.session.add(comment)
        # recent_user = User.query.filter(User.email == user.email).first()
        #
        # assert(recent_user.request.first().comment.first() == comment)

