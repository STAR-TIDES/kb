'''
star_tides.services.databases.mongo.models.engagement_model

Objects and utilities for working with "engagement" data (e.g. what areas of
interest a contact is interested in) at the database level.
'''

from mongoengine import EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentListField, ListField, StringField
from star_tides.services.databases.mongo.models.location_model import LocationModel

class EngagementModel(EmbeddedDocument):
    '''
    Engagement model for attaching engagement information to a model via a
    mongoengine.EmbeddedDocumentfield.
    '''

    locations = EmbeddedDocumentListField(LocationModel, required=True)
    backgrounds = ListField(StringField(min_length=1),required=True)
    areas_of_interest = ListField(StringField(min_length=1),required=True)
    focuses = ListField(StringField(min_length=1), required=True)

