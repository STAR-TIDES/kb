''' star_tides.tests.fixtures.basic_user
'''
import pytest
import bcrypt
from star_tides.services.mongo.models.user_model import User


@pytest.fixture()
def basic_user():
    ''' Basic fixture for a user.
    '''

    created_users = []

    def _basic_user(
            first_name='Test',
            last_name='User',
            email='test_user@example.com',
            password='password'
    ):

        password = password.encode('utf-8')

        salt = bcrypt.gensalt()
        h = bcrypt.hashpw(password, salt)

        u = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=h
        )
        u.save()

        created_users.append(u)

    yield _basic_user

    for user in created_users:
        user.delete()



