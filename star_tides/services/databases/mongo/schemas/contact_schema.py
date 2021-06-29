''' star_tides.services.databases.mongo.schemas.contact_schema
'''
from star_tides.services.databases.mongo.schemas.location_schema import LocationSchema
from star_tides.services.databases.mongo.schemas.engagement_schema import EngagementSchema
from star_tides.services.databases.mongo.models.availability import Availability
from marshmallow_enum import EnumField
from marshmallow.utils import EXCLUDE
from marshmallow import Schema, fields


class ContactSchema(Schema):
    '''ContactSchema is the Marshmallow schema subclass for contacts.'''
    id = fields.String(required=False, missing=None)
    user_id = fields.String(required=False, missing=None)
    name = fields.String(required=True)
    email = fields.Email(required=False, missing=None)
    phone_number = fields.String(required=False, missing=None)
    job_title = fields.String(required=False, missing=None)
    website_url = fields.Url(required=False, missing=None)
    location = fields.Nested(LocationSchema, required=True)
    languages = fields.List(fields.String())
    availability = EnumField(Availability, required=True)
    engagement = fields.Nested(EngagementSchema, required=True)
    statuses = fields.List(fields.String(), required=False)
    # TODO(i/15): Add this back in once the Marshmallow handling of
    # update_timestamps is fixed.
    # update_timestamps = fields.List(fields.Nested(UpdateTimestampSchema))

    class Meta:
        unknown = EXCLUDE
