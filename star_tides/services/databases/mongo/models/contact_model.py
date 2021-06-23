'''
star_tides.services.databases.mongo.models.contact_model

ContactModel representing Contact objects in the MongoDB database.
'''

from mongoengine.base.fields import ObjectIdField
from mongoengine import Document, StringField, EmailField, URLField
from mongoengine.fields import EmbeddedDocumentField, EmbeddedDocumentListField, ListField, EnumField
from star_tides.services.databases.mongo.models.update_timestamp_model import UpdateTimestampModel
from star_tides.services.databases.mongo.models.location_model import LocationModel
from star_tides.services.databases.mongo.models.engagement_model import EngagementModel
from star_tides.services.databases.mongo.models.availability import Availability

class ContactModel(Document):
    '''Contact MongoDB model.'''

    user_id = ObjectIdField(required=False)
    name = StringField(required=True)
    email = EmailField(required=False)
    phone_number = StringField(required=False)
    job_title = StringField(required=False)
    website_url = URLField(required=False)
    location = EmbeddedDocumentField(LocationModel, required=True)
    languages = ListField(StringField(min_length=1), required=False)
    availability = EnumField(Availability, required=True)
    engagement = EmbeddedDocumentField(EngagementModel, required=True)
    statuses = ListField(StringField(min_length=1), required=False)

    # Append-only list of (user_id, timestamp) objects for edits on this
    # ContactModel object. The first item is the creation of this model.
    update_timestamps = EmbeddedDocumentListField(
        UpdateTimestampModel, required=True)

    # NOTE: Projects will link to this contact object,
    # not the other way around.
