''' star_tides.services.databases.mongo.schemas.project_schema
'''
from marshmallow.utils import EXCLUDE
from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from star_tides.services.databases.mongo.schemas import camelcase
from star_tides.services.databases.mongo.schemas.location_schema import LocationSchema
from star_tides.services.databases.mongo.schemas.engagement_schema import EngagementSchema
from star_tides.services.databases.mongo.models.project_status import ProjectStatus


class ProjectSchema(Schema):
    '''ProjectSchema is the Marshmallow schema subclass for Projects.'''
    name = fields.String(required=True)
    location = fields.Nested(LocationSchema, required=True)
    engagement = fields.Nested(EngagementSchema, required=True)
    contacts = fields.List(fields.String(), required=False)
    summary = fields.String(required=True)
    grants = fields.List(fields.String(), required=False)
    solution_costs = fields.String(required=False, missing=None)
    # TODO(ljr): Add this field back in once the Model/MongoEngine bug is fixed.
    # updates = fields.List(fields.Nested(UpdateSchema),
    #   required=False, missing=[])
    notes = fields.String(required=False, missing=None)
    status = EnumField(ProjectStatus, required=True)

    class Meta:
        unknown = EXCLUDE

    def on_bind_field(self, field_name: str, field_obj: fields.Field) -> None:
        field_obj.data_key = camelcase(field_obj.data_key or field_name)
