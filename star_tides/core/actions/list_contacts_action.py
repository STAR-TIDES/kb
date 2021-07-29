'''star_tides.core.actions.list_contacts_action
'''

from star_tides.config.settings import DEFAULT_PAGE_SIZE
from star_tides.core.data.contact_data import ContactData
from star_tides.core.actions.base_action import Action
from star_tides.services.databases.mongo.models.contact_model import ContactModel


class ListContactsAction(Action):
    def run(self):
        return [ContactData.from_model(model) for model in
                ContactModel.objects.order_by('name')[:DEFAULT_PAGE_SIZE]]
