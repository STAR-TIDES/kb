''' star_tides.core.actions.login_user_action
'''
from star_tides.core.actions.base_action import Action
from star_tides.core.actions.create_user_action import CreateUserAction
from star_tides.services.databases.mongo.models.user_model import UserModel
from star_tides.api.util.issue_jwt import create_jwt
from star_tides.utils.random_string import gen_rand_n_str
from star_tides.exceptions import ParamInvalidError
import bcrypt

from google.oauth2 import id_token
from google.auth.transport import requests
from flask import current_app
from collections import namedtuple


class LoginUserAction(Action):
    ''' Action to log in a user.

    This class logs a user in. Either a username and password or a google sign
    in token must be provided.

    Args:
        username: string or None. Currently the provided email
        password: string or None. The provided password
        token: string or None. A google sign in token used for verification.

    Returns:
        Response tuple ('jwt', 'refresh_token')

    Raises:
        UserNotFoundError: When provided with basic auth (email + password)
            no user with {email} was found.
    '''

    response = namedtuple('Response', ['jwt', 'refresh_token'])

    def __init__(self, username=None, password=None, token=None):
        self.username = username
        self.password = password
        self.token = token

    #
    def run(self):

        if not (self.token or (self.username and self.password)):
            raise ParamInvalidError(
                'Must use either token or username and password')

        if self.token:

            id_info = id_token.verify_oauth2_token(
                self.token,
                requests.Request(),
                current_app.config['CLIENT_ID']
            )
            email = id_info.get('email')

            if email is None:
                # TODO create a custom exception and raise it
                print(f'{self.__class__.__name__} No email in claims: {email}')
                # TODO: Remove return here in favor of a raised exception
                raise Exception('email not found from token')

            user = UserModel.objects(email=email).first()

            if user is None:
                print(f'{self.__class__.__name__} '
                      f'No account associated with email in claims: '
                      f'{email}\nCreating user'
                )

                first_name = id_info.get('given_name')
                last_name =  id_info.get('family_name')
                password = gen_rand_n_str(32)
                CreateUserAction(
                    first_name,
                    last_name,
                    email,
                    password
                ).execute()

                user = UserModel.objects(email=email).first()
                if user is None:
                    # TODO create a custom exception and raise it
                    raise Exception('User failed to create')

            return LoginUserAction.response(*create_jwt(user.email))

        password = self.password.encode('utf-8')
        user = UserModel.objects(email=self.username).first()

        if user is None:
            # TODO create a custom exception and raise it
            print(f'{self.__class__.__name__} User not found')

        if bcrypt.checkpw(password, user.password):
            # TODO create refresh token
            return LoginUserAction.response(*create_jwt(user.email))
        # TODO create a custom exception and raise it
        print(f'{self.__class__.__name__} Password not a match')
