'''star_tides.core.data.user_data
'''

from star_tides.services.databases.mongo.models.user_model import UserModel
from typing import NamedTuple, Optional, Text


class UserData(NamedTuple):
    '''UserData represents the non-secret data about a user in our system.
    '''
    first_name: Text
    last_name: Text
    email: Text

    contact_id: Optional[Text] = None

    @staticmethod
    def from_model(model: UserModel):
        d = model.to_mongo()
        del d['_id']
        d['id'] = str(model.id)

        return UserData(**d)
