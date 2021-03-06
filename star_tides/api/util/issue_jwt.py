''' star_tides.api.util.issue_jwt
'''
import jwt
from bson.objectid import ObjectId
from datetime import datetime, timedelta, timezone
from flask import current_app


def create_jwt(user_id: ObjectId) -> tuple:
    ''' Creates a jwt.

        @param user_id: The id element of the user object. `user.id`.

        returns
    '''
    now = datetime.now(timezone.utc)
    jwt_token = jwt.encode(
        {
            'iss': 'star-tides',
            'exp': now + timedelta(hours=1),
            'iat': now,
            'claims': {
                'id': str(user_id)
            }
        },
        current_app.config['SECRET_KEY']
    )

    weeks_per_month = 4

    refresh_token = jwt.encode(
        {
            'iss': 'star-tides',
            'exp': now + timedelta(weeks=weeks_per_month*6),
            'iat': now,
        },
        current_app.config['SECRET_KEY']
    )

    return jwt_token, refresh_token


def get_email_from_jwt(decoded_jwt: dict) -> str:
    return decoded_jwt['claims']['id']
