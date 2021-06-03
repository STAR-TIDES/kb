''' star_tides.api.controllers.base_controller

Contains the base class for all Controllers.

'''
from abc import ABCMeta, abstractmethod
from flask import request
import base64


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
    def execute(self):
        try: # pylint: disable=broad-except
            # log_dict = {'class_name': self.__class__.__name__,
            #             'endpoint': request.url,
            #             'request_method': request.method}
            # TODO: Convert to logging when logs are implemented.
            response = self.process_request()


        # TODO: Handle custom exceptions

        # TODO: Handle system exceptions
        except Exception as e:
            raise e

        return response

    @abstractmethod
    def process_request(self):
        # raise NotImplemented('Method not implemented.')
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
        # TODO exception
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
            raise e

        return user_id, password


