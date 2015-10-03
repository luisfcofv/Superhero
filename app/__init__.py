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

    from app.models import User
    # api = Api(app)
    #
    # from app.resources.auroras import Auroras, AuroraSingle
    # api.add_resource(Auroras, '/aurora/')
    # api.add_resource(AuroraSingle, '/aurora/<string:string_date>')

    return app
