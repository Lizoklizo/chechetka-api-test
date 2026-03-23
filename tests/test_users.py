import allure
import pytest
import uuid

from api.utils.assertions import assert_status_code, assert_has_data


@allure.feature("Users API")
@allure.story("Get all users")
@pytest.mark.api
@pytest.mark.smoke
def test_get_users_returns_200_and_data(users_service):
    response = users_service.get_all_users()

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0


@allure.feature("Users API")
@allure.story("Get user by id")
@pytest.mark.api
def test_get_user_by_id_returns_200(users_service):
    response = users_service.get_user(1)

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["id"] == 1


@allure.feature("Users API")
@allure.story("Search users")
@pytest.mark.api
def test_search_users_returns_200(users_service):
    response = users_service.search_user("john")

    assert_status_code(response, 200)

    body = response.json()
    assert "query" in body
    assert "total" in body
    assert "results" in body

    assert body["query"] == "john"
    assert isinstance(body["results"], list)
    assert body["total"] >= 1


@allure.feature("Users API")
@allure.story("Create user")
@pytest.mark.api
def test_create_user_returns_201(users_service):
    unique_suffix = uuid.uuid4().hex[:8]

    payload = {
        "name": f"Elizaveta Test {unique_suffix}",
        "username": f"elizaveta_test_{unique_suffix}",
        "email": f"elizaveta.{unique_suffix}@example.com",
    }

    response = users_service.create_user(payload)

    assert_status_code(response, 201)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["name"] == payload["name"]
    assert body["data"]["email"] == payload["email"]


@allure.feature("Users API")
@allure.story("Put user")
@pytest.mark.api
def test_put_user_returns_200(users_service):
    payload = {
        "name": "Updated User",
        "username": "updateduser",
        "email": "updated.user@example.com",
    }

    response = users_service.replace_user(1, payload)

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["name"] == payload["name"]
    assert body["data"]["email"] == payload["email"]

@allure.feature("Users API")
@allure.story("Patch user - not supported by API (returns 404)")
@pytest.mark.api
def test_patch_user_not_supported_returns_404(users_service):
    # PATCH /users не поддерживается apimocker — документируем это поведение
    payload = {"name": "Patched User"}

    response = users_service.update_user_partially(2, payload)

    assert_status_code(response, 404)

    body = response.json()
    assert "error" in body


@allure.feature("Users API")
@allure.story("Delete user")
@pytest.mark.api
def test_delete_user_returns_204(users_service):
    # Берём последнего юзера из списка чтобы не сломать другие тесты
    list_response = users_service.get_all_users()
    last_id = list_response.json()["data"][-1]["id"]

    response = users_service.remove_user(last_id)

    assert_status_code(response, 204)