''' star_tides.services.databases.mongo.models.guidance_model
'''
from mongoengine import (
    EmbeddedDocument,
    StringField,
    ObjectIdField,
    EmbeddedDocumentField,
    URLField
)
from star_tides.services.databases.mongo.models.location_model import (
    LocationModel
)


class Guidance(EmbeddedDocument):
    author = ObjectIdField(required=False)
    project_id = ObjectIdField(required=False)
    text_content = StringField(required=False)
    link = URLField(required=False)
    location = EmbeddedDocumentField(LocationModel, required=True)
