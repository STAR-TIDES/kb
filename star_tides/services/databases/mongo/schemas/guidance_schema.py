from star_tides.services.databases.mongo.models.guide_model import Guide
from star_tides.services.databases.mongo.schemas.location_schema import LocationSchema
from marshmallow import Schema, fields, validates, post_load


class GuidanceSchema(Schema):
    id = fields.String(attribute='id', dump_only=True)
    author = fields.String(required=True)
    project_id = fields.String(required=False)
    text_content = fields.String(required=False)
    link = fields.String(required=False)
    geo_location = fields.Nested(LocationSchema, required=False)

    @post_load
    def make_guide(self, data, **kwargs):
        new_guide = Guide(**data)
        new_guide.save()
        return new_guide

    @validates('related_projects')
    def validate_related_projects(self, value):
        for uuid in value:
            uuid_str = str(uuid)
        return value

    @validates('relevant_contracts')
    def validate_relevant_contracts(self, value):
        for uuid in value:
            uuid_str = str(uuid)
        return value


class GuideUpdateSchema(GuideSchema):
    name = fields.String(required=False)
    guidance = fields.String(required=False)