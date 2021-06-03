''' star_tides.tests.fixtures.basic_user
'''
import pytest
import bcrypt
from star_tides.constants import UserTypes
from star_tides.services.databases.mongo.models.user_model import UserModel
from star_tides.services.databases.mongo.schemas.user_schema import UserSchema
from star_tides.utils.random_string import gen_rand_n_str


@pytest.fixture()
def basic_user():
    ''' Basic fixture for a user.
    '''

    created_users = []

    def _basic_user(
            first_name=f'Test-{gen_rand_n_str(3)}',
            last_name=f'User-{gen_rand_n_str(3)}',
            email=f'{gen_rand_n_str(8)}@example.com',
            password='password',
            kb_privilege=UserTypes.COLLABORATOR
    ):

        password = password.encode('utf-8')

        salt = bcrypt.gensalt()
        h = bcrypt.hashpw(password, salt)

        u = UserModel(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=h,
            kb_privilege=kb_privilege
        )
        u.save()

        created_users.append(u)

        return UserSchema().dump(u)

    yield _basic_user

    for user in created_users:
        user.delete()



