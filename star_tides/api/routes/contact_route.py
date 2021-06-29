'''star_tides.api.routes.contact_route
'''

from star_tides.api.controllers.contact_controller import CreateContactController, GetContactController, ListContactsController
from star_tides.api.routes import build_response
from flask import Blueprint

contact = Blueprint('contact', __name__, url_prefix='/contacts')

@contact.route('/', methods=['GET'])
def list_contacts():
    return build_response(ListContactsController().execute())

@contact.route('/<contact_id>', methods=['GET'])
def get_contact(contact_id: str):
    return build_response(GetContactController(contact_id).execute())

# FIXME(ljr): Add login_required.
@contact.route('/', methods=['POST'])
def create_contact():
    return build_response(CreateContactController().execute())

