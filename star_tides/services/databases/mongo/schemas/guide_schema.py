''' star_tides.services.databases.mongo.schemas.guide_schema
'''
from star_tides.services.databases.mongo.models.guide_model import Guide
from star_tides.services.databases.mongo.schemas.guidance_schema import GuidanceSchema
from marshmallow import Schema, fields, validates, post_load


class GuideSchema(Schema):
    ''' Schema for the guide object
    '''
    id = fields.String(attribute='id', dump_only=True)
    name = fields.String(required=True)
    guidance = fields.Nested(GuidanceSchema, required=True)
    focuses = fields.List(fields.String(), required=False)
    related_projects = fields.List(fields.UUID(), required=False)
    relevant_contracts = fields.List(fields.UUID(), required=False)

    @post_load
    def make_guide(self, data):
        new_guide = Guide(**data)
        new_guide.save()
        return new_guide

    @validates('related_projects')
    def validate_related_projects(self, value):
        for uuid in value:
            uuid_str = str(uuid)
            print(uuid_str)
        return value

    @validates('relevant_contracts')
    def validate_relevant_contracts(self, value):
        for uuid in value:
            uuid_str = str(uuid)
            print(uuid_str)
        return value


# class GuideUpdateSchema(GuideSchema):
#     name = fields.String(required=False)
#     guidance = fields.Nested(GuidanceSchema, required=False)
