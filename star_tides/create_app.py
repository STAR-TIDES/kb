''' star_tides.create_app

Contains application factory for the flask app.

'''
from flask import Flask
from mongoengine import connect
from star_tides.api.blueprint import bp
from star_tides.api.routes.base_route import base
from star_tides.api.routes.auth_route import auth
from star_tides.api.routes.contact_route import contact
import os


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object('star_tides.config.settings')
    app.config['SECRET_KEY'] = os.environ.get('SECRET') or 'secret_key'

    connect(
        username=os.getenv('MONGO_INITDB_ROOT_USERNAME'),
        password=os.getenv('MONGO_INITDB_ROOT_PASSWORD'),
        host='mongodb://mongodb_container:27017/star_tides?authSource=admin'
    )

    app.register_blueprint(bp)
    app.register_blueprint(base)
    app.register_blueprint(auth)
    app.register_blueprint(contact)

    return app
