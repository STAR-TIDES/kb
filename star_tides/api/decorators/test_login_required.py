''' star_tides.api.decorators.test_login_required
'''
# Disabled because pytest adds fixtures by having them specified as arguments.
# This overloads the import which isn't allowed in google's pylintrc.
# pragma pylint: disable=W0621,W0613,W0611,W0703

import base64
from star_tides.tests.utils import response_to_dict
from star_tides.tests.conftest import client
from star_tides.tests.fixtures.basic_user import basic_user


def test_login_required_decorator(client, basic_user):

    try:
        # Should fail because we haven't set headers.
        response = client.get('/test_route')
        assert False
    # Will need to be updated when we have an exceptions framework made.
    # TODO Issue 38
    except Exception:
        pass

    # Considering wrapping authed routes in a function because
    # this is too much to write every time we want to authenticate
    user = basic_user()
    email = user['email']

    encoded_email_and_password = \
        base64.b64encode(bytes(f'{email}:password', 'utf-8'))

    header = {'Authorization': 'Basic {}'.format(
        encoded_email_and_password.decode('utf-8'))}

    response = client.post('/auth/login',
                           headers=header)

    response_body = response_to_dict(response)

    response = client.get('/test_route',
               headers={'Authorization': f'Bearer {response_body["jwt"]}'})

    assert response.status_code == 200
