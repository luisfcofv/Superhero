from app import db


class CompanyPostalCode(db.Model):
    __tablename__ = 'company_postal_code'
    id = db.Column(db.Integer, primary_key=True)
    postal_code_id = db.Column(db.Integer, db.ForeignKey('postal_codes.id'))
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
