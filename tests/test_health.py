import allure
import pytest

from api.utils.assertions import assert_status_code


@allure.feature("Health")
@allure.story("Health check")
@pytest.mark.api
@pytest.mark.smoke
def test_health_returns_200(session):
    with allure.step("GET /health"):
        response = session.get("https://apimocker.com/health")

    assert_status_code(response, 200)

    body = response.json()
    assert "status" in body