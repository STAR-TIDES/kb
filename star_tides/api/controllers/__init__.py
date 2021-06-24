'''star_tides.api.controllers.__init__
'''

import string

from mongoengine.errors import ValidationError

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

