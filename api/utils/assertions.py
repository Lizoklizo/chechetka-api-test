def assert_status_code(response, expected_code: int):
    assert response.status_code == expected_code, (
        f"Expected status code {expected_code}, got {response.status_code}. "
        f"Response body: {response.text}"
    )


def assert_has_data(response_json: dict):
    assert "data" in response_json, (
        f"Response does not contain 'data': {response_json}"
    )