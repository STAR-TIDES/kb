'''star_tides.core.action.get_contact_action
'''
from mongoengine.errors import DoesNotExist
from star_tides.exceptions import NotFoundError
from star_tides.core.data.contact_data import ContactData
from star_tides.services.databases.mongo.models.contact_model import ContactModel
from star_tides.core.actions.base_action import Action


class GetContactAction(Action):
    '''
    GetContactAction fetches the Contact from the database using the given ID.
    '''

    def __init__(self, contact_id: str) -> None:
        self.contact_id = contact_id

    def run(self):
        try:
            model = ContactModel.objects.get(id=self.contact_id)
        except DoesNotExist as e:
            raise NotFoundError(
                f'Could not find contact with ID {self.contact_id}.') from e
        return ContactData.from_model(model)
