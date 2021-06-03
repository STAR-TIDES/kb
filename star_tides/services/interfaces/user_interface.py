''' star_tides.services.interfaces.user_interface
'''
from star_tides.services.interfaces.utils.interface_decorator import (
    interface_decorator
)
from star_tides.constants import UserTypes
from star_tides.services.databases.mongo.models.user_model import UserModel
from star_tides.services.databases.mongo.schemas.user_schema import UserSchema


class UserInterface:
    ''' Contains methods pertaining to the user collection
    '''

    @classmethod
    @interface_decorator
    def create_user(cls,
                    first_name: str,
                    last_name: str,
                    email: str,
                    pw_hash: bytes,
                    kb_privilege: int = UserTypes.COLLABORATOR,
                    only: list = None) -> dict:
        ''' Creates a user.

        Args:
            first_name - The first name of the user to be created.
            last_name - The last name of the user to be created.
            email - The email of the new user. Note that this variable has the
                constraint that it has to be unique.
            pw_hash - The salted and hashed byte-string of the user's password.
            kb_privilege - The level of privilege this user will have.

        Returns:
            A dictionary representing the created user.

        Raises:
            TODO: Should raise an exception if user.save() errors out.
            TODO: Implement UserExistsException
        '''
        user = UserModel(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=pw_hash,
            kb_privilege=kb_privilege
        )
        user.save()
        return UserSchema(only=only).dump(user)

    @classmethod
    @interface_decorator
    def get_user(cls,
                 user_id: str = None,
                 email: str = None,
                 only: list = None) -> dict:
        ''' Returns a user. You can query on a user id (_id in an object),
        or an email as they're both unique keys.

        Args:
            user_id - the _id key of a user object to search for
            email - the email of the user object to search for
        Returns:
            Dictionary representing the user object. The id and
            kb_privilege fields are omitted by the schema.

        Raises:
            TODO: UserNotFoundException
        '''
        user = None

        if user_id:
            user = UserModel.objects(id=user_id).first()
        elif email:
            user = UserModel.objects(email=email)

        return UserSchema(only=only).dump(user)
