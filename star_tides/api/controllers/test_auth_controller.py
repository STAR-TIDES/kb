''' star_tides.api.routes.test_auth_route
'''
# Disabled because pytest adds fixtures by having them specified as arguments.
# This overloads the import which isn't allowed in google's pylintrc.
# pragma pylint: disable=W0621,W0613,W0611

from star_tides.services.mongo.models.user_model import User
from star_tides.tests.conftest import client


def test_user_creation(client):
    # TODO: Implement this test.
    pass
