''' star_tides.api.controllers.base_controller

Contains the base class for all Controllers.

'''
from collections import namedtuple
from abc import ABCMeta, abstractmethod
from flask import request, current_app
from star_tides.exceptions import StarTidesException
from star_tides.api.controllers import build_response
import base64
import jwt
from http import HTTPStatus


class Controller(metaclass=ABCMeta):
    ''' Controller base class.

    Every controller should override the `process_request()` method.
    Designing controllers and actions this way allows for easy request logging,
    a standard invocation following the command pattern, etc.

    Only the path parameters should be passed in to a controller because we
    (currently or plan to in the future) leverage static methods to access
    query parameters, the request body, cookies, headers, etc.

    The overridden `process_request` method should return a serialized response.

    Invocation:
        response = ChildClassController(*args, **kwargs).execute()

    Helper static methods:

    * get_request_body
    * process_basic_auth
    * decode_basic_auth
    and more to come!
    '''

    response = namedtuple('Response', 'response http_code')

    def execute(self):
        try: # pylint: disable=broad-except
            # log_dict = {'class_name': self.__class__.__name__,
            #             'endpoint': request.url,
            #             'request_method': request.method}
            # TODO: Convert to logging when logs are implemented. Issue 27
            # number.
            res, error_code = self.process_request()

        except StarTidesException as e:
            res = e
            error_code = e.http_code
        except Exception as e:  # pylint: disable=broad-except
            res = {'error': str(e)}
            error_code = HTTPStatus.INTERNAL_SERVER_ERROR

        response = Controller.response(res, error_code)

        return build_response(response)

    @abstractmethod
    def process_request(self):
        pass

    @staticmethod
    def get_request_body(body_type='json'):

        body = None

        if body_type == 'json':
            body = request.get_json()
        elif body_type == 'form':
            body = request.form

        return body

    @staticmethod
    def process_basic_auth():
        try: # pylint: disable=broad-except
            auth = request.headers.get('Authorization')
            encoded = auth.split(' ')[1]
            username, password = Controller.decode_basic_auth(encoded)

            return username, password
        # TODO exception Issue 38
        except Exception as e:
            raise e

    @staticmethod
    def decode_basic_auth(auth_string):
        try:
            credentials_bytes = base64.b64decode(auth_string)
            credentials = credentials_bytes.decode('utf-8')
            credentials_parts = credentials.split(':')

            user_id = credentials_parts[0]
            password = credentials_parts[1]
        except Exception as e:
            # TODO Issue 38 handle exception
            raise e

        return user_id, password

    @staticmethod
    def decode_jwt() -> dict:
        # TODO create exceptions for authorization Issue 38
        token = None
        decoded_jwt = None

        header = request.headers.get('Authorization')
        if header is None:
            raise Exception('No Authorization header present.')
        try:
            token = header.split(' ')[1]
        except IndexError as e:
            raise Exception('Invalid authorization header.') from e

        try:
            decoded_jwt = jwt.decode(
                token, algorithms=['HS256'],
                key=current_app.config['SECRET_KEY']
            )
        except jwt.exceptions.InvalidSignatureError as e:
            raise Exception('Signature is invalid.') from e

        return decoded_jwt


