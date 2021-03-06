''' star_tides.api.controllers.auth_controller
'''
from star_tides.api.controllers.base_controller import Controller
from star_tides.core.actions.login_user_action import (
    LoginUserAction,
    CreateUserAction
)


class LoginController(Controller):
    ''' Controller to handle basic auth login (username and password)
    '''
    def process_request(self) -> dict:
        username, password = self.process_basic_auth()
        jwt, refresh = LoginUserAction(username, password).execute()
        return {
            'jwt': jwt,
            'refresh_token': refresh,
        }


class CreateUserController(Controller):
    ''' Controller to create a user.

    Args:
        first_name: string. First name of user.
        last_name: string. Last name of user.
        email: string. Email of user.
        password: string. Password of user.

    Returns:
        String jwt of current user's login session.

    '''
    def process_request(self) -> dict:
        body = self.get_request_body()
        first_name = body.get('first_name')
        last_name = body.get('last_name')
        email = body.get('email')
        password = body.get('password')

        return CreateUserAction(
            first_name,
            last_name,
            email,
            password
        ).execute()


class GoogleSignInController(Controller):
    ''' Controller to handle Google SSO login.

    Args:
        idtoken - string. Google id token.

    Returns:
        JWT for the current user.

    '''
    def process_request(self) -> dict:
        body = self.get_request_body(body_type='form')

        jwt, refresh = LoginUserAction(token=body.get('idtoken')).execute()

        return {
            'jwt': jwt,
            'refresh': refresh
        }
