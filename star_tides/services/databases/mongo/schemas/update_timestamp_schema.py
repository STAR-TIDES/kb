'''star_tides.services.databases.mongo.schemas.update_timestamp_schema
'''

from marshmallow import Schema, fields


class UpdateTimestampSchema(Schema):
    timestamp = fields.DateTime(required=True)
    user_id = fields.String(required=True)
