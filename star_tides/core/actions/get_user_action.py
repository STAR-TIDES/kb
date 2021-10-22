'''star_tides.core.actions.get_user_action
'''

from star_tides.core.data.user_data import UserData
from star_tides.services.databases.mongo.models.user_model import UserModel
from star_tides.core.actions.base_action import Action


class GetUserAction(Action):
    def __init__(self, user_id: str) -> None:
        self.user_id = user_id

    def run(self) -> UserData:
        model = UserModel.objects.get(id=self.user_id)
        return UserData.from_model(model)
