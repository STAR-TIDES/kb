''' star_tides.core.actions.create_user_action
'''
from star_tides.core.actions.base_action import Action
from star_tides.services.interfaces.user_interface import UserInterface
import bcrypt


class CreateUserAction(Action):
    ''' Action to create a user

    Args:
        first_name: string. First name of the user.
        last_name: string. Last name of the user.
        email: string. Email of the user.
        password: string. Password of the user.

    Returns:
        A dictionary of the created user

    Raises:
        None

    '''
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def run(self) -> dict:
        salt = bcrypt.gensalt()
        self.password = self.password.encode('utf-8')
        pw_hash = bcrypt.hashpw(self.password, salt)
        user = UserInterface.create_user(
            self.first_name,
            self.last_name,
            self.email,
            pw_hash
        )
        return user
