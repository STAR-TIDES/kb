'''star_tides.core.actions.update_contact_action
'''

from star_tides.core.actions.get_contact_action import GetContactAction
from star_tides.core.actions.base_action import Action
from star_tides.core.data.contact_data import ContactData
from star_tides.services.databases.mongo.models.contact_model import ContactModel
from star_tides.services.databases.mongo.schemas.contact_schema import ContactSchema


class UpdateContactAction(Action):
    '''UpdateContactAction updates a single contact in the DB using the given
    contact_id and updates dictionary of values to update.
    '''

    def __init__(self, contact_id: str, updates: dict) -> None:
        self.contact_id = contact_id
        self.updates = updates

    def run(self):
        # TODO(i/15): Update update_timestamps.
        # ContactModel.objects(id=self.contact_id).update_one()
        old_contact = GetContactAction(self.contact_id).run()
        merged_contact = old_contact._replace(**self.updates)
        schema = ContactSchema(partial=True).load(merged_contact._asdict())
        updated_model = ContactModel.objects(
            id=self.contact_id).modify(**schema, new=True)
        return ContactData.from_model(updated_model)
