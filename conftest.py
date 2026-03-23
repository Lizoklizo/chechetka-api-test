import pytest
import requests

from api.clients.users_client import UsersClient
from api.services.users_service import UsersService


@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    yield s
    s.close()


@pytest.fixture
def users_client(session):
    return UsersClient(session)


@pytest.fixture
def users_service(users_client):
    return UsersService(users_client)