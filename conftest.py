import pytest
import requests

from api.clients.users_client import UsersClient
from api.clients.posts_client import PostsClient
from api.clients.todos_client import TodosClient
from api.services.users_service import UsersService
from api.services.posts_service import PostsService
from api.services.todos_service import TodosService

from api.clients.comments_client import CommentsClient
from api.services.comments_service import CommentsService


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


@pytest.fixture
def posts_client(session):
    return PostsClient(session)


@pytest.fixture
def posts_service(posts_client):
    return PostsService(posts_client)


@pytest.fixture
def todos_client(session):
    return TodosClient(session)


@pytest.fixture
def todos_service(todos_client):
    return TodosService(todos_client)

@pytest.fixture
def comments_client(session):
    return CommentsClient(session)


@pytest.fixture
def comments_service(comments_client):
    return CommentsService(comments_client)