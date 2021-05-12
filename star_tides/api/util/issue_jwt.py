import jwt
import time
from flask import current_app


def create_jwt(email):

    now = int(time.time())

    return jwt.encode({
        'iss': 'star-tides',
        'exp': now + 3600,
        'iat': now,
        'aud': [f'email:{email}']
        },
        current_app.config['SECRET_KEY']
    )

