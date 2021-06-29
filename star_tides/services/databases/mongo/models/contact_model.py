'''
star_tides.services.databases.mongo.models.contact_model

ContactModel representing Contact objects in the MongoDB database.
'''

from mongoengine.base.fields import ObjectIdField
from mongoengine import Document, StringField, EmailField, URLField
from mongoengine.fields import EmbeddedDocumentField, EnumField, ListField
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

    # TODO(i/15): Marshmallow can't handle this field, so for now, remove
    # it until we figure out how to make it work (and read-only)
    # in ContactSchema.
    #
    # Append-only list of (user_id, timestamp) objects for edits on this
    # ContactModel object. The first item is the creation of this model.
    # update_timestamps =
    # EmbeddedDocumentListField( UpdateTimestampModel, required=True)

    # NOTE: Projects will link to this contact object,
    # not the other way around.
