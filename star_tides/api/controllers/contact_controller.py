'''star_tides.api.controllers.contact_controller
'''

from star_tides.exceptions import InvalidParamError
from star_tides.core.actions.update_contact_action import UpdateContactAction
from star_tides.core.actions.delete_contact_action import DeleteContactAction
from star_tides.core.data.contact_data import ContactData
from star_tides.core.actions.create_contact_action import CreateContactAction
from star_tides.api.controllers import snake_case_dict, validate_document_id
from star_tides.core.actions.get_contact_action import GetContactAction
from star_tides.core.actions.list_contacts_action import ListContactsAction
from star_tides.api.controllers.base_controller import Controller


class ListContactsController(Controller):
    def process_request(self) -> dict:
        contacts = ListContactsAction().run()
        return {
            'contacts': [contact._asdict() for contact in contacts],
        }


class GetContactController(Controller):
    def __init__(self, contact_id: str) -> None:
        self.contact_id = contact_id

    def process_request(self) -> dict:
        validate_document_id(self.contact_id)
        contact = GetContactAction(self.contact_id).run()
        return contact._asdict()


class CreateContactController(Controller):
    '''Creates a Contact in the DB given the JSON body in the request.'''

    def process_request(self) -> dict:
        body = self.get_request_body()
        if not body:
            raise InvalidParamError('Expected JSON body to be present.')
        json_body = snake_case_dict(body)
        # TODO(ljr): Pass to ContactSchema first?
        parsed_contact = ContactData(**json_body)
        created_contact = CreateContactAction(
            # TODO(ljr): Pass the caller user email.
            parsed_contact, unused_caller_user_email='').run()
        return created_contact._asdict()


class DeleteContactController(Controller):
    def __init__(self, contact_id: str) -> None:
        self.contact_id = contact_id

    def process_request(self):
        validate_document_id(self.contact_id)
        DeleteContactAction(self.contact_id).run()
        return {}


class UpdateContactController(Controller):
    def __init__(self, contact_id: str) -> None:
        self.contact_id = contact_id

    def process_request(self):
        validate_document_id(self.contact_id)
        updated_contact = UpdateContactAction(
            self.contact_id, self.get_request_body()).run()
        return updated_contact._asdict()
