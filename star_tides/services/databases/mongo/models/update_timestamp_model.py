'''star_tides.services.databases.mongo.models.update_timestamp_model
'''

from mongoengine.base.fields import ObjectIdField
from mongoengine.document import EmbeddedDocument
from mongoengine.fields import DateTimeField


class UpdateTimestampModel(EmbeddedDocument):
    timestamp = DateTimeField(required=True)
    user_id = ObjectIdField(required=True)
