'''star_tides.api.controllers.__init__
'''

import string

from mongoengine.errors import ValidationError

def validate_document_id(given_id: str) -> None:
    '''
    Validates that the given_id is a valid Mongo DB Document Object ID.
    '''
    all_hex = all(c in string.hexdigits for c in given_id)
    if not (all_hex and len(given_id) == 24):
        raise Exception(
            f'expected `{given_id}` to be a 24 character hex string')

