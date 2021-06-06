''' star_tides.api.blueprint

This module contains the main blueprint for star_tides.

'''

from flask import Blueprint
from star_tides.api.decorators.login_required import login_required
bp = Blueprint('bp', __name__)


@bp.route('/test_route')
@login_required
def index():
    return "It's an app yo"
