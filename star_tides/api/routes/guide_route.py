''' star_tides.api.routes.guide_route
'''
from star_tides.api.decorators.login_required import login_required
from star_tides.api.controllers.guide_controller import (
    CreateGuideController,
    ListGuidesController,
    GetGuideController,
    DeleteGuideController,
    UpdateGuideController
)
from flask import Blueprint

guide = Blueprint('guide', __name__, url_prefix='/guides')


@guide.route('/', methods=['GET'])
def list_guides():
    response = ListGuidesController().execute()
    return response


@guide.route('/<guide_id>', methods=['GET'])
def list_contacts(guide_id):
    response = GetGuideController(guide_id).execute()
    return response


@guide.route('/', methods=['POST'])
# @login_required
def create_contact():
    response = CreateGuideController().execute()
    return response


@guide.route('/<guide_id>', methods=['DELETE'])
@login_required
def delete_contact(guide_id: str):
    response = DeleteGuideController(guide_id).execute()
    return response


@guide.route('/<guide_id>', methods=['PUT'])
@login_required
def update_contact(guide_id: str):
    response = UpdateGuideController(guide_id).execute()
    return response

