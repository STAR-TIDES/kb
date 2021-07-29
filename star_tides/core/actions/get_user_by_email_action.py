'''star_tides.core.actions.get_user_by_email_action
'''

from mongoengine.errors import DoesNotExist
from star_tides.core.actions.base_action import Action
from star_tides.services.databases.mongo.models.user_model import UserModel
from star_tides.core.data.user_data import UserData
from star_tides.exceptions import NotFoundError


class GetUserByEmailAction(Action):
    '''Action that fetches a user given their email.'''

    def __init__(self, email: str) -> None:
        self.email = email

    def run(self) -> UserData:
        try:
            model = UserModel.object.get(email=self.email)
        except DoesNotExist as e:
            raise NotFoundError(
                f'Could not find user with email {self.email}') from e
        return UserData.from_model(model)
