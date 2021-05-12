from mongoengine import Document, StringField, BinaryField


class User(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = BinaryField(required=False)



