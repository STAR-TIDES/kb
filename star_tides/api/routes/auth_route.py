from flask import Blueprint
from star_tides.api.controllers.auth_controller import LoginController, CreateUserController, GoogleSignInController
from flask import render_template

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=["POST"])
def login():
    response = LoginController().execute()
    return str(response)

@auth.route('/new/user', methods=["POST"])
def create_user():
    response = CreateUserController().execute()
    return response

@auth.route('/gsignin', methods=["GET"])
def gsignin():
    return render_template('google_signin.html')

@auth.route('/sso/google', methods=["POST"])
def auth_google_sign_in():
    response = GoogleSignInController().execute()
    print(response)
    return response

