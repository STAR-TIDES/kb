from abc import ABCMeta, abstractmethod
from flask import request
import base64

class Controller(metaclass=ABCMeta):

    def execute(self):
        try:
            response = self.process_request()
        except Exception as e:
            raise e
        return response

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
        try:
            auth = request.headers.get('Authorization')
            encoded = auth.split(' ')[1]
            username, password = Controller.decode_basic_auth(encoded)

            return username, password
        except Exception as e:
            pass

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


