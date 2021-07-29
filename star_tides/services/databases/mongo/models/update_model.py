'''star_tides.services.databases.mongo.models.update_model
'''

from mongoengine import EmbeddedDocument
from mongoengine.fields import DateTimeField, ObjectIdField, StringField


class UpdateModel(EmbeddedDocument):
    timestamp = DateTimeField(required=True)
    user_id = ObjectIdField(required=True)
    # Links to the contact that requested this update.
    requesting_contact_id = ObjectIdField(required=False)
    content = StringField(required=True)
