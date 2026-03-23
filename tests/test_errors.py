import allure
import pytest


from api.utils.assertions import assert_status_code


@allure.feature("Error Handling")
@allure.story("404 Not Found")
@pytest.mark.api
def test_error_404(session):
    with allure.step("GET /error/404"):
        response = session.get("https://apimocker.com/error/404")

    assert_status_code(response, 404)

    body = response.json()
    assert "error" in body
    assert body["error"] == "Not Found"


@allure.feature("Error Handling")
@allure.story("500 Server Error")
@pytest.mark.api
def test_error_500(session):
    with allure.step("GET /error/500"):
        response = session.get("https://apimocker.com/error/500")

    assert_status_code(response, 500)

    body = response.json()
    assert "error" in body


@allure.feature("Error Handling")
@allure.story("Validation Error")
@pytest.mark.api
def test_error_validation(session):
    with allure.step("GET /error/validation"):
        response = session.get("https://apimocker.com/error/validation")

    assert_status_code(response, 400)

    body = response.json()
    assert "error" in body


@allure.feature("Error Handling")
@allure.story("404 Not Found")
@pytest.mark.api
def test_get_nonexistent_user_returns_404(users_service):
    response = users_service.get_user(999999)

    assert_status_code(response, 404)

    body = response.json()
    assert "error" in body


@allure.feature("Error Handling")
@allure.story("404 Not Found")
@pytest.mark.api
def test_get_nonexistent_post_returns_404(posts_service):
    response = posts_service.get_post(999999)

    assert_status_code(response, 404)

    body = response.json()
    assert "error" in body


@allure.feature("Error Handling")
@allure.story("Validation Error")
@pytest.mark.api
def test_create_user_without_required_fields_returns_400(users_service):
    response = users_service.create_user({})

    assert_status_code(response, 400)

    body = response.json()
    assert "error" in body


@allure.feature("Error Handling")
@allure.story("Validation Error")
@pytest.mark.api
def test_create_post_without_required_fields_returns_400(posts_service):
    response = posts_service.create_post({})

    assert_status_code(response, 400)

    body = response.json()
    assert "error" in body