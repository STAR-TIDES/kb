'''star_tides.services.databases.mongo.schemas.location_schema
'''

from marshmallow import Schema, fields


class LocationSchema(Schema):
    iso_3166_1_country_code = fields.Integer(required=True)
    arbitrary_text = fields.String(required=False)
