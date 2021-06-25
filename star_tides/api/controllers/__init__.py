''' star_tides.api.controllers
'''
import json
from http import HTTPStatus
from typing import Union
from flask import Response
from star_tides.exceptions import StarTidesException


def build_response(
        response: Union[dict, StarTidesException],
        status_code: int = HTTPStatus.OK
    ) -> Response:
    ''' Builds a flask JSON response.

        Args:
            response - Can be a dictionary or a StarTidesException.
            status_code - defaults to 200.

        Returns:
            Response - a flask response mimetyped to application/json
    '''

    response_payload = None
    response_status_code = status_code

    if isinstance(response, dict):
        response_payload = json.dumps(response)
    elif isinstance(response, StarTidesException):
        response_status_code = response.http_code
        data = response.__dict__
        data.pop('logging_msg')
        data.pop('severity')
        response_payload = json.dumps(data)

    return Response(
        response_payload,
        mimetype='application/json',
        status=response_status_code
    )
