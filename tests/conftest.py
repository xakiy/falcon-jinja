import pytest
from falcon.testing import TestClient

from .helpers import application


@pytest.fixture()
def client():
    return TestClient(application.app)


@pytest.fixture()
def jinja_context():
    return {'quote': 'Hello from Falcon!'}


@pytest.fixture()
def jinja_array_context():
    return {'frameworks': ['Falcon', 'Flask', 'Django']}
