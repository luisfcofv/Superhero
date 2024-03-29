from app.models import Company
from flask_restful import Resource


class Products(Resource):
    def get(self, company_id):
        company = Company.query.get(company_id)

        if company is None:
            return 'Company not found', 400

        products_array = []
        for product in company.products:
            products_array.append(product.dictionary())

        return products_array
