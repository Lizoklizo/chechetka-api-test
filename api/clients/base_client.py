import json
from typing import Any, Dict, Optional

import allure
import requests

from api.utils.config import BASE_URL, REQUEST_TIMEOUT
from api.utils.logger import get_logger


class BaseClient:
    def __init__(self, session: requests.Session):
        self.session = session
        self.base_url = BASE_URL
        self.timeout = REQUEST_TIMEOUT
        self.logger = get_logger(self.__class__.__name__)

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        url = f"{self.base_url}{endpoint}"

        self.logger.info(
            "Request: %s %s | params=%s | json=%s",
            method,
            url,
            params,
            json_body,
        )

        with allure.step(f"{method} {endpoint}"):
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json_body,
                timeout=self.timeout,
            )

            self.logger.info(
                "Response: %s | status=%s",
                url,
                response.status_code,
            )

            allure.attach(
                json.dumps(
                    {
                        "method": method,
                        "url": url,
                        "params": params,
                        "json": json_body,
                    },
                    ensure_ascii=False,
                    indent=2,
                ),
                name="request",
                attachment_type=allure.attachment_type.JSON,
            )

            try:
                response_body = response.json()
                allure.attach(
                    json.dumps(response_body, ensure_ascii=False, indent=2),
                    name="response",
                    attachment_type=allure.attachment_type.JSON,
                )
            except Exception:
                allure.attach(
                    response.text,
                    name="response",
                    attachment_type=allure.attachment_type.TEXT,
                )

            return response

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint: str, json_body: Dict[str, Any]) -> requests.Response:
        return self._request("POST", endpoint, json_body=json_body)

    def put(self, endpoint: str, json_body: Dict[str, Any]) -> requests.Response:
        return self._request("PUT", endpoint, json_body=json_body)

    def patch(self, endpoint: str, json_body: Dict[str, Any]) -> requests.Response:
        return self._request("PATCH", endpoint, json_body=json_body)

    def delete(self, endpoint: str) -> requests.Response:
        return self._request("DELETE", endpoint)