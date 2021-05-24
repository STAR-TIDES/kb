''' star_tides.services.mongo.models.user_model
'''
from mongoengine import Document, StringField, BinaryField, IntField


class User(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = BinaryField(required=False)
    kb_privilege = IntField(required=True, default=0)
    jwt = StringField(required=True, default='')
    refresh_token = StringField(required=True, default='')



