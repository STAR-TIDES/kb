''' star_tides.tests.conftest.py
'''
import pytest
from star_tides.create_app import create_app


@pytest.fixture()
def client():
    ''' All fixtures in conftest.py will be used in every fixture in the
    test package.
    '''
    app = create_app()

    with app.test_client() as app_client:
        yield app_client
