''' star_tides.config.settings

Flask application settings.

'''
import os

STATIC_FOLDER = '../app/dist/star-tides/'
CLIENT_ID = os.getenv('CLIENT_ID')
