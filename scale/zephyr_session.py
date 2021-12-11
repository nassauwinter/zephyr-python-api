import logging

from requests import Session
from urllib.parse import urlparse, parse_qs


DEFAULT_BASE_URL = "https://api.zephyrscale.smartbear.com/v2/"


class ZephyrSession(object):
    def __init__(self, token: str, base_url: str = DEFAULT_BASE_URL):
        self.base_url = base_url
        self.s = Session()
        self.s.headers.update({"Authorization": f"Bearer {token}"})
        self.logger = logging.getLogger(__name__)

    def _create_url(self, *args):
        return self.base_url + "/".join(args)

    def _request(self, method: str, endpoint: str, **kwargs):
        self.logger.debug(f"{method.capitalize()} data to {endpoint=} and {kwargs}")
        url = self._create_url(endpoint)
        response = self.s.request(method=method, url=url, **kwargs)
        result = response.json() if response.content else ""
        if response.status_code < 400:
            return result
        else:
            raise Exception(f"Error {response.status_code}. Response: {result}")

    def get(self, endpoint: str, params: dict = None):
        return self._request("get", endpoint, params=params)

    def post(self, endpoint: str, json: dict = None):
        return self._request("post", endpoint, json=json)

    def put(self, endpoint: str, json: dict = None):
        return self._request("put", endpoint, json=json)

    def delete(self, endpoint: str):
        return self._request("delete", endpoint)

    def get_paginated(self, endpoint, params=None):
        """Get paginated data"""
        self.logger.debug(f"Get paginated data from {endpoint=} and {params=}")
        if params is None:
            params = {}

        while True:
            response = self.get(endpoint, params=params)
            if "values" not in response:
                return
            for value in response.get("values", []):
                yield value
            if response.get("isLast") is True:
                break
            params_str = urlparse(response.get("next")).query
            params.update(parse_qs(params_str))
        return
