from config import config
from flask import Flask
from flask_restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from app.models import User, Order
    api = Api(app)

    from app.resources.users import Users, SingleUser
    from app.resources.companies import Companies, SingleCompany
    from app.resources.products import Products

    api.add_resource(Users, '/users')
    api.add_resource(SingleUser, '/users/<string:user_id>')
    api.add_resource(Companies, '/restaurants')
    api.add_resource(SingleCompany, '/restaurants/<string:company_id>')
    api.add_resource(Products, '/restaurants/<string:company_id>/products')

    return app
