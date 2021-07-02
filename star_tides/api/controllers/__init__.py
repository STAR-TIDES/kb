''' star_tides.api.controllers
'''
import json
from typing import NamedTuple
from flask import Response
from star_tides.exceptions import StarTidesException


def build_response(response: NamedTuple) -> Response:
    ''' Builds a flask JSON response.

        Args:
            response - Can be a dictionary or a StarTidesException.
            status_code - defaults to 200.

        Returns:
            Response - a flask response mimetyped to application/json
    '''

    response_payload = None

    if isinstance(response.response, dict):
        response_status_code = response.http_code
        response_payload = json.dumps(response.response)
    elif isinstance(response.response, StarTidesException):
        response_status_code = response.http_code
        data = response.response.__dict__
        data.pop('logging_msg')
        data.pop('severity')
        response_payload = json.dumps(data)
    return Response(
        response_payload,
        mimetype='application/json',
        status=response_status_code
    )
