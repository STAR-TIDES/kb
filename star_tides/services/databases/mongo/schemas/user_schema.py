''' star_tides.services.databases.mongo.schemas.user_schema
'''
import marshmallow_mongoengine as ma
from star_tides.services.databases.mongo.models.user_model import UserModel


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        exclude = ['password', 'kb_privilege']
