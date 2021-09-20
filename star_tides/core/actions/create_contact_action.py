'''star_tides.core.action.create_contact_action
'''

from star_tides.services.databases.mongo.schemas.contact_schema import ContactSchema
from star_tides.services.databases.mongo.models.contact_model import ContactModel
from star_tides.core.data.contact_data import ContactData
from star_tides.core.actions.base_action import Action
from star_tides.exceptions import InvalidParamError


class CreateContactAction(Action):
    '''
    CreateContactAction creates the given Contact in the database and
    returns the saved copy.
    '''

    def __init__(self, contact: ContactData,
                 unused_caller_user_email: str) -> None:
        self.contact = contact

    def run(self):
        if self.contact.id is not None:
            raise InvalidParamError(
                response_msg='Expected contact not to have ID.')
        # TODO(i/15): Add this back in once ContactSchema works with the
        # update_timestamps field.
        #
        # self.contact.update_timestamps.append(
        #     UpdateTimestampData(timestamp=datetime.now(),
        #                         user_id=id_from_caller_user_email))
        schema = ContactSchema().load(self.contact._asdict())
        saved_model = ContactModel(**schema, _created=True).save()
        return ContactData.from_model(saved_model)
