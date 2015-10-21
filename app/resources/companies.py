from app.models import Company, PostalCode, CompanyPostalCode
from flask_restful import Resource


class Companies(Resource):
    def get(self):
        companies = Company.query.all()

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


class CompaniesByPostalCode(Resource):
    def get(self, country_code, postal_code):
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


