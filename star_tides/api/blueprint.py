''' star_tides.api.blueprint

This module contains the main blueprint for star_tides.

'''

from flask import Blueprint
bp = Blueprint('bp', __name__)


@bp.route('/')
def index():
    return "It's an app yo"
