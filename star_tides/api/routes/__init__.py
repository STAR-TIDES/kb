''' star_tides.api.routes
'''
import json
from flask import Response


def build_response(response, status_code=200):
    return Response(
        json.dumps(response),
        mimetype='application/json',
        status=status_code
    )
