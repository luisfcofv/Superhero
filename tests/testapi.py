import requests
from app import db
from tests.testbase import TestBase


class TestDB(TestBase):

    def test_insert_requests(self):
        data = {

        }
        # r = requests.post("http://0.0.0.0:5000/users/1/requests", data={"key":"value"})
