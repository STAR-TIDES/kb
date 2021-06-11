''' star_tides.api.decorators.login_required
'''

# TODO Implement a decorator to enforce login
from functools import wraps
from star_tides.api.controllers.base_controller import Controller
import time


def login_required(func):
    ''' This decorator enforces that a request is authenticated with the server
        in any way other than unauthenticated.

        Args:
            func - function

        Returns: Should return responses
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        now = int(time.time())
        try:
            jwt = Controller.decode_jwt()
            if now > jwt['exp']:
                # TODO return 401 response Issue 38.
                raise Exception('expired jwt. Use refresh token or re-login')
        except Exception as e:
            # TODO handle the various exceptions from decode_jwt. Issue 38
            # TODO build 401 response.
            raise Exception('Jwt invalid. Use refresh token or re-login') from e
        return func(*args, **kwargs)

    return wrapper

