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
    api = Api(app)

    # TODO Api endpoints
    return app



