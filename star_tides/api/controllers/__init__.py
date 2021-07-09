''' star_tides.api.controllers
'''
import json
from http import HTTPStatus
from typing import NamedTuple
from flask import Response


class ControllerResponse(NamedTuple):
    response: dict
    http_code: HTTPStatus


def build_response(response: ControllerResponse) -> Response:
    ''' Builds a flask JSON response.

        Args:
            response - response object from base_controller
        Returns:
            Response - a flask response mimetyped to application/json
    '''
    return Response(
        json.dumps(response.response),
        mimetype='application/json',
        status=response.http_code
    )
