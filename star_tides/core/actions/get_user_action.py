'''
star_ides.api.core.actions.get_user_action
'''

from typing import Text
from star_tides.core.actions.base_action import Action
from star_tides.db.users import UsersCollection
import json

class GetUserAction(Action):
    def __init__(self, user_id: Text) -> None:
        super().__init__()
        self.user_id = user_id
        self.users_collection = UsersCollection()

    def run(self):
        user = self.users_collection.get_user(self.user_id)
        return json.dumps(user.to_dict())
