from flask import Flask, render_template
from mongoengine import connect
from celery import Celery
from star_tides.api.blueprint import bp
from star_tides.api.routes.auth_route import auth
import os



def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object('star_tides.config.settings')
    app.config['SECRET_KEY'] = os.environ.get('SECRET') or "secret_key"

    db.init_app(app)

    connect(
        username='evan',
        password='password',
        host='mongodb://mongodb_container:27017/star_tides?authSource=star_tides'
    )

    @app.route('/')
    def index():
        return render_template('index.html')

    app.register_blueprint(bp)
    app.register_blueprint(auth)

    return app