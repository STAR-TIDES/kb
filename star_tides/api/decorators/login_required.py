''' star_tides.api.decorators.login_required
'''

# TODO Implement a decorator to enforce login
from functools import wraps
from star_tides.exceptions import AuthenticationError, StarTidesException
from star_tides.config.settings import UNSAFE_IGNORE_LOGIN_REQUIRED
from star_tides.api.controllers.base_controller import Controller
import traceback


def login_required(func):
    ''' This decorator enforces that a request is authenticated with the server
        in any way other than unauthenticated.

        Args:
            func - the route function.

        Returns: Should return responses.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if UNSAFE_IGNORE_LOGIN_REQUIRED:
            # TODO(ljr): Make this a log instead.
            print('login_required functionality is disabled')
        else:
            try:
                # If the JWT is invalid (e.g. expired, can't be decoded),
                # this code will raise an exception.
                Controller.decode_jwt()
            except Exception as e:
                return {
                    'error': str(e),
                    'errorClass': e.__class__.__name__
                }
        return func(*args, **kwargs)

    return wrapper
