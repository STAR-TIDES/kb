'''
star_tides.services.databases.mongo.models.contact_model

ContactModel representing Contact objects in the MongoDB database.
'''

from mongoengine import Document, StringField, EmailField, UUIDField, URLField
from mongoengine.fields import EmbeddedDocumentField, ListField, EnumField
from star_tides.services.databases.mongo.models.location_model import LocationModel
from star_tides.services.databases.mongo.models.engagement_model import EngagementModel
from star_tides.services.databases.mongo.models.availability import Availability

class ContactModel(Document):
    '''Contact MongoDB model.'''

    user_id = UUIDField(binary=False, required=False)
    name = StringField(required=True)
    email = EmailField(required=False)
    phone_number = StringField(required=False)
    job_title = StringField(required=False)
    website_url = URLField(required=False)
    location = EmbeddedDocumentField(LocationModel, required=True)
    languages = ListField(required=False)
    availability = EnumField(Availability, required=True)
    engagement = EmbeddedDocumentField(EngagementModel, required=True)
    statuses = ListField(required=False)

    # Append-only list of (user_id, timestamp) objects for edits on this
    # ContactModel object. The first item is the creation of this model.
    update_timestamps = ListField(required=True)

    # NOTE: Projects will link to this contact object,
    # not the other way around.
