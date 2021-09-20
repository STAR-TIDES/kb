'''star_tides.api.routes.contact_route
'''

from star_tides.api.controllers.contact_controller import CreateContactController, DeleteContactController, GetContactController, ListContactsController, UpdateContactController
from star_tides.api.routes import build_response
from flask import Blueprint

contact = Blueprint('contact', __name__, url_prefix='/contacts')


@contact.route('/', methods=['GET'])
def list_contacts():
    return build_response(ListContactsController().execute())


@contact.route('/<contact_id>', methods=['GET'])
def get_contact(contact_id: str):
    return build_response(GetContactController(contact_id).execute())


@contact.route('/', methods=['POST'])
def create_contact():
    # FIXME(ljr): Add login_required.
    return build_response(CreateContactController().execute())


@contact.route('/<contact_id>', methods=['DELETE'])
def delete_contact(contact_id: str):
    # FIXME(ljr): Add login_required.
    return build_response(DeleteContactController(contact_id).execute())


@contact.route('/<contact_id>', methods=['PUT'])
def update_contact(contact_id: str):
    # FIXME(ljr): Add login_required.
    return build_response(UpdateContactController(contact_id).execute())
