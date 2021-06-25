''' star_tides.api.routes.test_auth_route
'''
# Disabled because pytest adds fixtures by having them specified as arguments.
# This overloads the import which isn't allowed in google's pylintrc.
# pragma pylint: disable=W0621,W0613,W0611, W0105
import base64
from star_tides.tests.conftest import client
from star_tides.services.databases.mongo.models.user_model import UserModel
from star_tides.tests.fixtures.basic_user import basic_user
from star_tides.tests.utils import response_to_dict
from star_tides.utils.random_string import gen_rand_n_str

"""
def test_create_user(client):
    ''' Tests creating a user.
    '''
    first_name = gen_rand_n_str(8)
    last_name = gen_rand_n_str(8)
    email = f'{gen_rand_n_str(8)}@{gen_rand_n_str(8)}.com'
    password = gen_rand_n_str(8)

    body = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password
    }

    response = client.post('/auth/new/user', json=body)
    assert response.status_code == 200, 'test_create_user status code did not' \
                                        ' match.'

    response_data = response_to_dict(response)
    assert response_data[
               'first_name'] == first_name, 'test_create_user first name' \
                                            ' did not match'
    assert response_data['last_name'] == last_name, 'test_create_user ' \
                                                    ' last name did not match'
    assert response_data['email'] == email
    UserModel.objects(email=email).delete()

    assert UserModel.objects(email=email).first() is None


def test_login_user(client, basic_user):
    ''' Tests logging in a basic user
    '''

    user = basic_user()
    email = user['email']

    encoded_email_and_password = \
        base64.b64encode(bytes(f'{email}:password', 'utf-8'))

    header = {'Authorization': 'Basic {}'.format(
        encoded_email_and_password.decode('utf-8'))}

    response = client.post('/auth/login',
                           headers=header)

    response_body = response_to_dict(response)

    assert isinstance(response_body.get('jwt'), str)
    assert isinstance(response_body.get('refresh_token'), str)
"""
