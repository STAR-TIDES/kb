'''star_tides.services.databases.mongo.schemas.engagement_schema
'''

from marshmallow import Schema, fields
from star_tides.services.databases.mongo.schemas.location_schema import LocationSchema


class EngagementSchema(Schema):
    locations = fields.List(fields.Nested(LocationSchema), required=True)
    backgrounds = fields.List(fields.String(), required=True)
    areas_of_interest = fields.List(fields.String(), required=True)
    focuses = fields.List(fields.String(), required=True)
