from flask import Blueprint
bp = Blueprint('bp', __name__)


@bp.route('/')
def index():
    return "It's an app yo"