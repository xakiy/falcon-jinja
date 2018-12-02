import pytest
from bs4 import BeautifulSoup
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


@pytest.fixture()
def soup():
    def wrapper(html_text):
        return BeautifulSoup(html_text, 'html.parser')
    return wrapper
