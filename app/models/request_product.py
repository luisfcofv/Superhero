from app import db


class RequestProduct(db.Model):
    __tablename__ = 'request_products'
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('requests.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
