'''star_tides.core.actions.list_contacts_action
'''

from star_tides.core.actions.base_action import Action
from star_tides.services.databases.mongo.models.contact_model import ContactModel


class ListContactsAction(Action):
    def run(self):
        return ContactModel.objects
