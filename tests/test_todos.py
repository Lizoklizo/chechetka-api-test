import allure
import pytest
import uuid

from api.utils.assertions import assert_status_code, assert_has_data


@allure.feature("Todos API")
@allure.story("Get all todos")
@pytest.mark.api
@pytest.mark.smoke
def test_get_todos_returns_200_and_data(todos_service):
    response = todos_service.get_all_todos()

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0


@allure.feature("Todos API")
@allure.story("Get todo by id")
@pytest.mark.api
def test_get_todo_by_id_returns_200(todos_service):
    list_response = todos_service.get_all_todos()
    first_id = list_response.json()["data"][0]["id"]

    response = todos_service.get_todo(first_id)

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["id"] == first_id


@allure.feature("Todos API")
@allure.story("Filter completed todos")
@pytest.mark.api
def test_get_completed_todos_returns_200(todos_service):
    response = todos_service.get_all_todos(params={"completed": "true"})

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    for todo in body["data"]:
        assert todo["completed"] is True


@allure.feature("Todos API")
@allure.story("Delay simulation")
@pytest.mark.api
def test_todos_with_delay_returns_200(todos_service):
    response = todos_service.get_all_todos(params={"_delay": 1000})

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)


@allure.feature("Todos API")
@allure.story("Create todo")
@pytest.mark.api
def test_create_todo_returns_201(todos_service):
    unique_suffix = uuid.uuid4().hex[:8]

    payload = {
        "title": f"Test Todo {unique_suffix}",
        "completed": False,
    }

    response = todos_service.create_todo(payload)

    assert_status_code(response, 201)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["title"] == payload["title"]
    assert body["data"]["completed"] == payload["completed"]


@allure.feature("Todos API")
@allure.story("Put todo")
@pytest.mark.api
def test_put_todo_returns_200(todos_service):
    list_response = todos_service.get_all_todos()
    first_id = list_response.json()["data"][0]["id"]

    payload = {
        "title": "Updated Todo",
        "completed": True,
    }

    response = todos_service.replace_todo(first_id, payload)

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["title"] == payload["title"]
    assert body["data"]["completed"] == payload["completed"]


@allure.feature("Todos API")
@allure.story("Patch todo")
@pytest.mark.api
def test_patch_todo_completed_returns_200(todos_service):
    list_response = todos_service.get_all_todos()
    first_id = list_response.json()["data"][0]["id"]

    payload = {
        "title": "Patched Todo Title",
        "completed": True,
    }

    response = todos_service.update_todo(first_id, payload)

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["completed"] is True


@allure.feature("Todos API")
@allure.story("Delete todo")
@pytest.mark.api
def test_delete_todo_returns_204(todos_service):
    list_response = todos_service.get_all_todos()
    last_id = list_response.json()["data"][-1]["id"]

    response = todos_service.delete_todo(last_id)

    assert_status_code(response, 204)