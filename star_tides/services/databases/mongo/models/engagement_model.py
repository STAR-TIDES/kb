'''Objects and utilities for working with "engagement" data (e.g. what areas of
interest a contact is interested in) at the database level.
'''

from mongoengine import EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentListField, ListField
from .location_model import LocationModel

class EngagementModel(EmbeddedDocument):
    '''
    Engagement model for attaching engagement information to a model via a
    mongoengine.EmbeddedDocumentfield.
    '''

    locations = EmbeddedDocumentListField(LocationModel, required=True)
    backgrounds = ListField(required=True)
    areas_of_interest = ListField(required=True)
    focuses = ListField(required=True)

