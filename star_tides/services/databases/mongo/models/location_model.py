'''Objects and utilities for working with geographic locations at the database
level.
'''

from mongoengine import EmbeddedDocument, IntField, StringField

class LocationModel(EmbeddedDocument):
    '''Location model for attaching geographic information to a model via a
    mongoengine.EmbeddedDocumentField.
    '''

    iso_3166_1_country_code = IntField(required=True)
    arbitrary_text = StringField(required=False)
