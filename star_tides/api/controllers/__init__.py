''' star_tides.api.controllers
'''
import json
from http import HTTPStatus
import re
from typing import NamedTuple
from flask import Response
import string
from star_tides.exceptions import InvalidParamError


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
        json.dumps(response.response) + '\n',
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
        raise InvalidParamError(
            f'expected `{given_id}` to be a 24 character hex string')


_snake_case_pattern = re.compile(r'(?<!^)(?=[A-Z])')


def _to_snake_case(s: str) -> str:
    return _snake_case_pattern.sub('_', s).lower()


# This function is used to convert JSON payload keys into snake_case from
# standard camelCase.
# TODO(ljr): We should probably just be using this marshmallow functionality:
# https://marshmallow.readthedocs.io/en/stable/examples.html#inflection-camel-casing-keys
def snake_case_dict(d: dict) -> dict:
    return {_to_snake_case(k): v for (k, v) in d.items()}
