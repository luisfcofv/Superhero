from app.models import Company, PostalCode, CompanyPostalCode
from flask_restful import Resource, reqparse


class Companies(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('country')
        parser.add_argument('postal_code')
        args = parser.parse_args()

        country_code = args.get('country')
        postal_code = args.get('postal_code')

        company_query = Company.query

        if country_code is not None:
            company_query = company_query.filter(Company.country_code == country_code)

        if country_code is not None and postal_code is not None:
            postal_code = PostalCode.query.filter(PostalCode.country_code == country_code,
                                                  PostalCode.postal_code == postal_code).first()

            if postal_code is None:
                return 'Country code or postal code not found', 400

            company_postal_codes = CompanyPostalCode.query.filter(CompanyPostalCode.postal_code_id == postal_code.id).all()
            response = []
            for company_postal_code in company_postal_codes:
                company = Company.query.get(company_postal_code.company.id)
                response.append(company.dictionary())

            return response
        else:
            companies = company_query.all()

            companies_array = []
            for company in companies:
                companies_array.append(company.dictionary())

            return companies_array


class SingleCompany(Resource):
    def get(self, company_id):
        company = Company.query.get(company_id)

        if company is None:
            return 'Company not found', 400

        return company.dictionary()
