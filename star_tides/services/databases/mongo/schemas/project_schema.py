''' star_tides.services.databases.mongo.schemas.project_schema
'''
from marshmallow.utils import EXCLUDE
from marshmallow import Schema


class ProjectSchema(Schema):
    '''ProjectSchema is the Marshmallow schema subclass for Projects.'''
    # FIXME(ljr): implement this schema

    class Meta:
        unknown = EXCLUDE
