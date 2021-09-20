''' star_tides.create_app

Contains application factory for the flask app.

'''
from flask import Flask
from mongoengine import connect
from star_tides.api.blueprint import bp
from star_tides.api.routes.auth_route import auth
from star_tides.api.routes.contact_route import contact
import os


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object('star_tides.config.settings')
    app.config['SECRET_KEY'] = os.environ.get('SECRET', 'secret_key')

    db_domain = os.environ.get('DB_DOMAIN', 'mongodb_container')
    db_port = os.environ.get('DB_PORT', '27017')
    db_name = os.environ.get('DB_NAME', 'star_tides')
    db_auth_source = os.environ.get('DB_AUTH_SOURCE', 'admin')


    resp = connect(
        username=os.getenv('MONGO_INITDB_ROOT_USERNAME'),
        password=os.getenv('MONGO_INITDB_ROOT_PASSWORD'),
        host=f'mongodb://'
             f'{db_domain}:{db_port}/{db_name}?authSource={db_auth_source}'
    )

    print(f'Resp is: {resp}')

    app.register_blueprint(bp)
    app.register_blueprint(auth)
    app.register_blueprint(contact)

    return app
