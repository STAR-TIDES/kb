''' star_tides.api.util.issue_jwt
'''
import jwt
import time
from flask import current_app


def create_jwt(email):
    seconds = 60
    minutes = 60
    hours = 24
    days = 7
    weeks = 4
    months = 6
    now = int(time.time())

    jwt_token = jwt.encode(
        {
            'iss': 'star-tides',
            'exp': now + seconds * minutes,
            'iat': now,
            'claims': {
                'email': email,
            }
        },
        current_app.config['SECRET_KEY']
    )

    # Refresh token valid for 6 months
    refresh_token = jwt.encode({
        'iss': 'star-tides',
        'exp': now + seconds * minutes * hours * days * weeks * months,
        'iat': now,
        },
        current_app.config['SECRET_KEY']
    )

    return jwt_token, refresh_token
