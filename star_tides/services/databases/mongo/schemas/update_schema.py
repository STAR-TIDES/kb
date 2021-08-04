'''star_tides.services.databases.mongo.schemas.update_schema
'''

from marshmallow import Schema, fields


class UpdateSchema(Schema):
    timestamp = fields.DateTime(required=True)
    user_id = fields.String(required=True)
    requesting_contact_id = fields.String(required=False)
    content = fields.String(required=True)
