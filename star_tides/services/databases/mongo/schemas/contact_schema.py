''' star_tides.services.databases.mongo.schemas.contact_schema
'''
import marshmallow_mongoengine as ma
from star_tides.services.databases.mongo.models.contact_model import ContactModel


class ContactSchema(ma.ModelSchema):
    class Meta:
        model = ContactModel

