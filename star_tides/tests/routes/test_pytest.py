''' star_tides.tests.tests.
'''
# pragma pylint: disable=W0621,W0613,W0611

from star_tides.tests.fixtures.basic_user import basic_user
from star_tides.services.mongo.models.user_model import User


def test_basic_test(client, basic_user):
    basic_user()

    u = User.objects(email="test_user@example.com").first()

    assert u is not None
    assert u.email == "test_user@example.com"

