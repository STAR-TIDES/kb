'''star_tides.api.routes.contact_route
'''

from star_tides.api.controllers.contact_controller import CreateContactController, DeleteContactController, GetContactController, ListContactsController, UpdateContactController
from star_tides.api.decorators.login_required import login_required
from flask import Blueprint

contact = Blueprint('contact', __name__, url_prefix='/contacts')


@contact.route('/', methods=['GET'])
def list_contacts():
    return ListContactsController().execute()


@contact.route('/<contact_id>', methods=['GET'])
def get_contact(contact_id: str):
    return GetContactController(contact_id).execute()


@contact.route('/', methods=['POST'])
@login_required
def create_contact():
    return CreateContactController().execute()


@contact.route('/<contact_id>', methods=['DELETE'])
@login_required
def delete_contact(contact_id: str):
    return DeleteContactController(contact_id).execute()


@contact.route('/<contact_id>', methods=['PUT'])
@login_required
def update_contact(contact_id: str):
    return UpdateContactController(contact_id).execute()
