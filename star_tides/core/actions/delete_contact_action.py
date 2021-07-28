'''star_tides.core.actions.delete_contact_action
'''

from star_tides.services.databases.mongo.models.contact_model import ContactModel
from star_tides.core.actions.base_action import Action


class DeleteContactAction(Action):
    def __init__(self, contact_id: str) -> None:
        self.contact_id = contact_id

    def run(self):
        ContactModel.objects.get(id=self.contact_id).delete()
