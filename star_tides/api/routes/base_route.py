'''
star_tides.api.routes.base_route
'''

import http
from flask import Blueprint, Response
import json
import datetime
import os

base = Blueprint('base', __name__)


@base.route('/', methods=['GET'])
def root():
    return Response(
        response=json.dumps({
            'date': str(datetime.datetime.now()),
            'tag': os.getenv('_VERSION_TAG'),
            'build': os.getenv('_VERSION_BUILD'),
        }),
        mimetype='application/json',
        status=http.HTTPStatus.OK,
    )
