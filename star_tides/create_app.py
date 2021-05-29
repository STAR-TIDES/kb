''' star_tides.create_app

Contains application factory for the flask app.

'''
from flask import Flask
from flask import send_from_directory
from mongoengine import connect
from star_tides.api.blueprint import bp
from star_tides.api.routes.auth_route import auth
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

    @app.route('/')
    def index():
        # os.system('ls -lR /app/static')
        # return send_from_directory('/app/static/', 'index.html')
        return 'pls use api'

    # @app.route('/static/')
    # def 

    # @app.route('/api/*')

    app.register_blueprint(bp)
    app.register_blueprint(auth)

    return app
