''' star_tides.services.mongo.models.user_model
'''
from mongoengine import (
    Document,
    StringField,
    UUIDField,
    ListField,
    EmbeddedDocumentField
)

from star_tides.services.databases.mongo.models.guidance_model import GuidanceModel


class UserModel(Document):
    ''' User model
    '''
    uuid = UUIDField(binary=False, required=False)
    name = StringField(required=True)
    focuses = ListField(required=True)
    related_projects = ListField(required=False, default=[])
    relevant_contracts = ListField(required=False, default=[])
    guidance = EmbeddedDocumentField(GuidanceModel, required=True)
