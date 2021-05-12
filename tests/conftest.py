import pytest

@pytest.fixture()
def client():
    from star_tides.create_app import create_app
    ''' All fixtures in conftest.py will be used in every fixture in the test package.
    '''
    app = create_app()

    with app.test_client() as app_client:
        yield app_client
