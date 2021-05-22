'''star_tides.core.actions.list_users_action
'''

from star_tides.core.actions.base_action import Action
import json
from star_tides.db.users import UsersCollection

class ListUsersAction(Action):
    def __init__(self):
        super().__init__()
        self.users_collection = UsersCollection()

    def run(self):
        users = self.users_collection.list_users()
        return json.dumps([user.to_dict() for user in users])
