''' star_tides.services.databases.mongo.models.guidance_model
'''
from mongoengine import (
    EmbeddedDocument,
    StringField,
    ObjectIdField,
    EmbeddedDocumentField
)
from star_tides.services.databases.mongo.models.location_model import (
    LocationModel
)


class Guidance(EmbeddedDocument):
    author = ObjectIdField(required=False)
    # TODO add project ID as a reference
    project_id = ObjectIdField(required=False, default='')
    text_content = StringField(required=False, default='')
    link = StringField(required=False, default='')
    geo_location = EmbeddedDocumentField(LocationModel, required=True)
