import logging

from requests import Session
from urllib.parse import urlparse, parse_qs


class ZephyrSession(object):
    def __init__(self, token: str, base_url: str):
        self.base_url = base_url
        self.s = Session()
        self.s.headers.update({"Authorization": f"Bearer {token}"})
        self.logger = logging.getLogger(__name__)

    def _create_url(self, *args):
        return self.base_url + "/".join(args)

    def _request(self, method: str, endpoint: str, return_raw: bool = False, **kwargs):
        self.logger.debug(f"{method.capitalize()} data: {endpoint=} and {kwargs}")
        url = self._create_url(endpoint)
        response = self.s.request(method=method, url=url, **kwargs)
        if response.status_code < 400:
            if return_raw:
                return response
            else:
                return response.json() if response.text else ""
        else:
            raise Exception(f"Error {response.status_code}. Response: {response.content}")

    def get(self, endpoint: str, params: dict = None, **kwargs):
        return self._request("get", endpoint, params=params, **kwargs)

    def post(self, endpoint: str, json: dict = None, **kwargs):
        return self._request("post", endpoint, json=json, **kwargs)

    def put(self, endpoint: str, json: dict = None, **kwargs):
        return self._request("put", endpoint, json=json, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._request("delete", endpoint, **kwargs)

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
