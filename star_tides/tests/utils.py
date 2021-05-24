''' star_tides.tests.utils
'''
from flask import Response
import json


def response_to_dict(response: Response) -> dict:
    ''' When testing a client, the response comes back as bytes.
    This deserializes it into a dictionary for use in assertions

    Args:
        response - the request's response
    Returns:
        A dictionary representing the json response from the test client.
    '''
    return json.loads(response.data.decode('utf-8'))
