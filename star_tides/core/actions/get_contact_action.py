'''star_tides.core.action.get_contact_action
'''
from star_tides.core.data.contact_data import ContactData
from star_tides.services.databases.mongo.models.contact_model import ContactModel
from star_tides.core.actions.base_action import Action

class GetContactAction(Action):
    '''
    GetContactAction fetches the Contact from the database using the given ID.
    '''
    def __init__(self, contact_id: str) -> None:
        super().__init__()
        self.contact_id = contact_id

    def run(self):
        model = ContactModel.objects.get(id=self.contact_id)
        return ContactData.from_model(model)
