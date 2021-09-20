'''star_tides.services.databases.mongo.schemas.location_schema
'''

from star_tides.services.databases.mongo.schemas import camelcase
from marshmallow import Schema, fields


class LocationSchema(Schema):
    iso_3166_1_country_code = fields.Integer(required=True)
    arbitrary_text = fields.String(required=False)

    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = camelcase(field_obj.data_key or field_name)
