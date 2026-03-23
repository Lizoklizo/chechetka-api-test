import allure
import pytest
import uuid

from api.utils.assertions import assert_status_code, assert_has_data


@allure.feature("Comments API")
@allure.story("Get all comments")
@pytest.mark.api
@pytest.mark.smoke
def test_get_comments_returns_200_and_data(comments_service):
    response = comments_service.get_all_comments()

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0


@allure.feature("Comments API")
@allure.story("Get comment by id")
@pytest.mark.api
def test_get_comment_by_id_returns_200(comments_service):
    list_response = comments_service.get_all_comments()
    first_id = list_response.json()["data"][0]["id"]

    response = comments_service.get_comment(first_id)

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["id"] == first_id


@allure.feature("Comments API")
@allure.story("Get comments with limit")
@pytest.mark.api
def test_get_comments_with_limit_returns_200(comments_service):
    response = comments_service.get_all_comments(params={"limit": 5})

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert isinstance(body["data"], list)
    assert len(body["data"]) <= 5


@allure.feature("Comments API")
@allure.story("Create comment")
@pytest.mark.api
def test_create_comment_returns_201(comments_service):
    unique_suffix = uuid.uuid4().hex[:8]

    payload = {
        "body": f"Test comment {unique_suffix}",
        "postId": 2,
        "name": f"Test User {unique_suffix}",
        "email": f"test.{unique_suffix}@example.com",
    }

    response = comments_service.create_comment(payload)

    assert_status_code(response, 201)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["body"] == payload["body"]
    assert body["data"]["postId"] == payload["postId"]


@allure.feature("Comments API")
@allure.story("Put comment")
@pytest.mark.api
def test_put_comment_returns_200(comments_service):
    list_response = comments_service.get_all_comments()
    first_id = list_response.json()["data"][0]["id"]

    unique_suffix = uuid.uuid4().hex[:8]

    payload = {
        "body": "Updated comment body",
        "postId": 2,
        "name": f"Updated User {unique_suffix}",
        "email": f"updated.{unique_suffix}@example.com",
    }

    response = comments_service.replace_comment(first_id, payload)

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["body"] == payload["body"]


@allure.feature("Comments API")
@allure.story("Patch comment")
@pytest.mark.api
def test_patch_comment_returns_200(comments_service):
    list_response = comments_service.get_all_comments()
    first_id = list_response.json()["data"][0]["id"]

    unique_suffix = uuid.uuid4().hex[:8]

    payload = {
        "body": "Patched comment body",
        "postId": 2,
        "name": f"Patched User {unique_suffix}",
        "email": f"patched.{unique_suffix}@example.com",
    }

    response = comments_service.update_comment_partially(first_id, payload)

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["body"] == payload["body"]


@allure.feature("Comments API")
@allure.story("Delete comment")
@pytest.mark.api
def test_delete_comment_returns_204(comments_service):
    list_response = comments_service.get_all_comments()
    last_id = list_response.json()["data"][-1]["id"]

    response = comments_service.remove_comment(last_id)

    assert_status_code(response, 204)