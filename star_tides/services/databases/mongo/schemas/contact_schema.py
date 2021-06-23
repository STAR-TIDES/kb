''' star_tides.services.databases.mongo.schemas.contact_schema
'''
import marshmallow_mongoengine as ma
import marshmallow_enum as mae
from star_tides.services.databases.mongo.models.contact_model import ContactModel
from star_tides.services.databases.mongo.models.availability import Availability


class ContactSchema(ma.ModelSchema):
    class Meta:
        model = ContactModel
        # FIXME(ljr): This is currently broken.
        # ma can't handle the model's EnumField and crashes.
        availability = mae.EnumField(Availability)
