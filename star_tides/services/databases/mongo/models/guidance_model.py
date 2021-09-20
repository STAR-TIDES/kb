''' star_tides.services.databases.mongo.models.guidance_model
'''
from mongoengine import EmbeddedDocument, StringField, ReferenceField
from star_tides.services.databases.mongo.models.contact_model import (
    ContactModel
)


class GuidanceModel(EmbeddedDocument):
    contact = ReferenceField(ContactModel, required=False)
    # TODO add project ID as a reference
    project_id = StringField()
    text_content = StringField(required=False, default='')
    link = StringField(required=False, default='')
    geo_location = StringField(required=False, default='')
