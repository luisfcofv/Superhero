import requests
import json
from tests.testbase import TestBase


class TestDB(TestBase):

    def test_insert_requests(self):
        data = [
            {"quantity": 3, "product_id": 1},
            {"quantity": 4, "product_id": 2}
        ]

        headers = {'content-type': 'application/json'}
        r = requests.post("http://0.0.0.0:5000/users/1/orders", data=json.dumps(data), headers=headers)
        print(r.json())
