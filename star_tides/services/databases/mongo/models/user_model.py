''' star_tides.services.mongo.models.user_model
'''
from mongoengine import Document, StringField, BinaryField, UUIDField, IntField


class UserModel(Document):
    ''' User model
    '''
    contact_id = UUIDField(binary=False, required=False)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = BinaryField(required=False)
    kb_privilege = IntField(required=True)
    current_jwt = StringField(required=True, default="")
    current_refresh_token = StringField(required=True, default="")
