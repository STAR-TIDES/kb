''' star_tides.api.routes.auth_route

Contains routes pertaining to authentication.

'''
from flask import Blueprint, render_template
from star_tides.api.routes import build_response
from star_tides.api.controllers.auth_controller import (
    # Uncomment when basic auth is added again.
    # LoginController,
    # CreateUserController,
    GoogleSignInController
)

auth = Blueprint('auth', __name__, url_prefix='/auth')


# @auth.route('/login', methods=['POST'])
# def login():
#     response = LoginController().execute()
#     return build_response(response)
#
#
# @auth.route('/new/user', methods=['POST'])
# def create_user():
#     response = CreateUserController().execute()
#     return build_response(response)


@auth.route('/gsignin', methods=['GET'])
def gsignin():
    return render_template('google_signin.html')


@auth.route('/sso/google', methods=['POST'])
def auth_google_sign_in():
    response = GoogleSignInController().execute()
    return build_response(response)
