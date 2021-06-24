''' star_tides.api.controllers
'''
import json
from http import HTTPStatus
from typing import NamedTuple
from flask import Response
import string

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


# This is the expected length of a Mongo DB Object ID.
_OBJECT_ID_LENGTH = 24

def validate_document_id(given_id: str) -> None:
    '''
    Validates that the given_id is a valid Mongo DB Document Object ID.
    '''
    all_hex = all(c in string.hexdigits for c in given_id)
    if not (all_hex and len(given_id) == _OBJECT_ID_LENGTH):
        # TODO(38): Throw a better exception that signals an HTTP invalid
        # argument code.
        raise Exception(
            f'expected `{given_id}` to be a 24 character hex string')
