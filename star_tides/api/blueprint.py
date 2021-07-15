''' star_tides.api.blueprint

This module is for testing.

'''
#  pylint: skip-file

from datetime import datetime
from flask import Blueprint
from star_tides.api.decorators.login_required import login_required
from star_tides.api.controllers import build_response
from star_tides.exceptions import AuthenticationError, InvalidParamError, StarTidesException
bp = Blueprint('bp', __name__)


@bp.route('/test_route')
@login_required
def index():
    return "It's an app yo"

@bp.route('/test_route/no_auth')
def index_no_auth():
    return f"It's an app yo [no auth] {datetime.now()}"
