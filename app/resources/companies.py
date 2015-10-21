from app.models import Company, PostalCode, CompanyPostalCode
from flask_restful import Resource


class Companies(Resource):
    def get(self, company_id):
        company = Company.query.get(company_id)
        return company.dictionary()


class CompaniesByPostalCode(Resource):
    def get(self, country_code, postal_code):
        postal_code = PostalCode.query.filter(PostalCode.country_code == country_code,
                                              PostalCode.postal_code == postal_code).first()

        company_postal_codes = CompanyPostalCode.query.filter(CompanyPostalCode.postal_code_id == postal_code.id).all()
        response = []
        for company_postal_code in company_postal_codes:
            company = Company.query.get(company_postal_code.company.id)
            response.append(company.dictionary())

        return response


