import allure
import pytest
import uuid

from api.utils.assertions import assert_status_code, assert_has_data


@allure.feature("Posts API")
@allure.story("Get all posts")
@pytest.mark.api
@pytest.mark.smoke
def test_get_posts_returns_200_and_data(posts_service):
    response = posts_service.get_all_posts()

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0


@allure.feature("Posts API")
@allure.story("Get post by id")
@pytest.mark.api
def test_get_post_by_id_returns_200(posts_service):
    response = posts_service.get_post(2)

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["id"] == 2


@allure.feature("Posts API")
@allure.story("Search posts")
@pytest.mark.api
def test_search_posts_returns_200(posts_service):
    response = posts_service.search_post("development")

    assert_status_code(response, 200)

    body = response.json()
    assert "query" in body
    assert "results" in body
    assert body["query"] == "development"
    assert isinstance(body["results"], list)


@allure.feature("Posts API")
@allure.story("Create post")
@pytest.mark.api
def test_create_post_returns_201(posts_service):
    unique_suffix = uuid.uuid4().hex[:8]

    payload = {
        "title": f"Test Post {unique_suffix}",
        "body": f"This is a test post body {unique_suffix}",
    }

    response = posts_service.create_post(payload)

    assert_status_code(response, 201)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["title"] == payload["title"]
    assert body["data"]["body"] == payload["body"]


@allure.feature("Posts API")
@allure.story("Put post")
@pytest.mark.api
def test_put_post_returns_200(posts_service):
    payload = {
        "title": "Updated Post Title",
        "body": "Updated post body content",
    }

    response = posts_service.replace_post(2, payload)

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["title"] == payload["title"]
    assert body["data"]["body"] == payload["body"]


@allure.feature("Posts API")
@allure.story("Patch post")
@pytest.mark.api
def test_patch_post_returns_200(posts_service):
    # API требует оба поля: title и body
    payload = {
        "title": "Patched Post Title",
        "body": "Patched post body content",
    }

    response = posts_service.update_post(2, payload)

    assert_status_code(response, 200)

    body = response.json()
    assert_has_data(body)
    assert body["data"]["title"] == payload["title"]


@allure.feature("Posts API")
@allure.story("Get post likes")
@pytest.mark.api
def test_get_post_likes_returns_200(posts_service):
    response = posts_service.get_post_likes(5)

    assert_status_code(response, 200)


@allure.feature("Posts API")
@allure.story("Delete post")
@pytest.mark.api
def test_delete_post_returns_204(posts_service):
    unique_suffix = uuid.uuid4().hex[:8]

    payload = {
        "title": f"Post to delete {unique_suffix}",
        "body": f"Temporary post body {unique_suffix}",
    }

    create_response = posts_service.create_post(payload)
    assert_status_code(create_response, 201)

    created_body = create_response.json()
    assert_has_data(created_body)

    post_id = created_body["data"]["id"]

    delete_response = posts_service.delete_post(post_id)
    assert_status_code(delete_response, 204)
