''' star_tides.core.actions.login_user_action
'''
from star_tides.core.actions.base_action import Action
from star_tides.core.actions.create_user_action import CreateUserAction
from star_tides.services.databases.mongo.models.user_model import UserModel
from star_tides.api.util.issue_jwt import create_jwt
from star_tides.utils.random_string import gen_rand_n_str
import bcrypt

from google.oauth2 import id_token
from google.auth.transport import requests
from flask import current_app


class LoginUserAction(Action):
    ''' Action to log in a user.

    This class logs a user in. Either a username and password or a google sign
    in token must be provided.

    Args:
        username: string or None. Currently the provided email
        password: string or None. The provided password
        token: string or None. A google sign in token used for verification.

    Returns:
        A signed JWT

    Raises:
        UserNotFoundError: When provided with basic auth (email + password)
            no user with {email} was found.
    '''
    def __init__(self, username=None, password=None, token=None):
        self.username = username
        self.password = password
        self.token = token

    def run(self) -> (str, str):
        if self.username and self.password:

            password = self.password.encode('utf-8')
            user = UserModel.objects(email=self.username).first()

            if user is None:
                # TODO create a custom exception and raise it
                print(f'{self.__class__.__name__} User not found')

            if bcrypt.checkpw(password, user.password):
                # TODO create refresh token
                return create_jwt(user.email), ''
            # TODO create a custom exception and raise it
            print(f'{self.__class__.__name__} Password not a match')
        elif self.token:
            idinfo = id_token.verify_oauth2_token(
                self.token,
                requests.Request(),
                current_app.config['CLIENT_ID']
            )
            email = idinfo.get('email')

            if email is None:
                # TODO create a custom exception and raise it
                print(f'{self.__class__.__name__} No email in claims: {email}')
                # TODO: Remove return here in favor of a raised exception
                return '', ''

            user = UserModel.objects(email=email).first()

            if user is None:
                print(f'{self.__class__.__name__} '
                      f'No account associated with email in claims: '
                      f'{email}\nCreating user'
                )

                first_name = idinfo.get('given_name')
                last_name =  idinfo.get('family_name')
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
                    print('User failed to create')

            return create_jwt(user.email), ''
