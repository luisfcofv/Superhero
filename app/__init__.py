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

    from app.models import User, Request
    api = Api(app)

    from app.resources.users import Users, SingleUser, UserRequest, Request
    from app.resources.requests import Requests, SingleRequest, RequestComment
    from app.resources.companies import Companies, CompaniesByPostalCode, SingleCompany

    api.add_resource(Users, '/user/')
    api.add_resource(SingleUser, '/user/<string:user_id>')
    api.add_resource(UserRequest, '/user/<string:user_id>/request')
    api.add_resource(Requests, '/request/')
    api.add_resource(SingleRequest, '/request/<int:request_id>')
    api.add_resource(RequestComment, '/request/<int:request_id>/comment')
    api.add_resource(CompaniesByPostalCode, '/company/<string:country_code>/<int:postal_code>')
    api.add_resource(Companies, '/company/')
    api.add_resource(SingleCompany, '/company/<string:company_id>')

    return app
