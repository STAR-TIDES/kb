'''star_tides.api.controllers.contact_controller
'''

from star_tides.services.databases.mongo.schemas.contact_schema import ContactSchema
from star_tides.api.controllers import validate_document_id
from star_tides.core.actions.get_contact_action import GetContactAction
from star_tides.core.actions.list_contacts_action import ListContactsAction
from star_tides.api.controllers.base_controller import Controller

class ListContactsController(Controller):
    def process_request(self) -> dict:
        return ContactSchema(many=True).dump(ListContactsAction().run())


class GetContactController(Controller):
    def __init__(self, contact_id: str) -> None:
        super().__init__()
        self.contact_id = contact_id

    def process_request(self) -> dict:
        validate_document_id(self.contact_id)
        contact = GetContactAction(self.contact_id).run()
        return ContactSchema().dump(contact)

