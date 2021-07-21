''' star_tides.config.settings

Flask application settings.

'''
import os

STATIC_FOLDER = '../app/dist/star-tides/'
CLIENT_ID = os.getenv('CLIENT_ID')
UNSAFE_IGNORE_LOGIN_REQUIRED = bool(os.getenv('UNSAFE_IGNORE_LOGIN_REQUIRED'))
