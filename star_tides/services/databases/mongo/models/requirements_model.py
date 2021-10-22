''' star_tides.services.databases.mongo.models.guidance_model
'''
from mongoengine import (
    EmbeddedDocument,
    StringField,
    IntField,
    EmbeddedDocumentField
)
from star_tides.services.databases.mongo.models.guidance_model import (
    GuidanceModel
)


class RequirementsModel(EmbeddedDocument):
    name = StringField(required=True)
    quantity = IntField(required=True)
    guidance = EmbeddedDocumentField(GuidanceModel, required=True)
