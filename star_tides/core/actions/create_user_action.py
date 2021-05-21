''' star_tides.core.actions.create_user_action
'''
from star_tides.core.actions.base_action import Action
from star_tides.services.mongo.models.user_model import User
import bcrypt


class CreateUserAction(Action):
    ''' Action to create a user

    Args:
        first_name: string. First name of the user.
        last_name: string. Last name of the user.
        email: string. Email of the user.
        password: string. Password of the user.

    Returns:
        True if successful.

    Raises:
        None

    '''
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def run(self):
        salt = bcrypt.gensalt()
        self.password = self.password.encode('utf-8')

        pw_hash = bcrypt.hashpw(self.password, salt)

        user = User(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            password=pw_hash
        )
        user.save()

        return True
