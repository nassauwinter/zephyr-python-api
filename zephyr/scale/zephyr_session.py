import logging

from requests import Session
from urllib.parse import urlparse, parse_qs


INIT_SESSION_MSG = "Initialize session by {}"


class ZephyrSession(object):
    def __init__(self, base_url, token=None, username=None, password=None, cookies=None):
        """
        Zephyr Scale basic session object.

        :param base_url: url to make requests to
        :param token: auth token
        :param username: username
        :param password: password
        :param cookies: cookie dict
        """
        self.base_url = base_url
        self.s = Session()
        self.logger = logging.getLogger(__name__)
        if token:
            self.logger.debug(INIT_SESSION_MSG.format("token"))
            self.s.headers.update({"Authorization": f"Bearer {token}"})
        elif username and password:
            self.logger.debug(INIT_SESSION_MSG.format("username and password"))
            self.s.auth = (username, password)
        elif cookies:
            self.logger.debug(INIT_SESSION_MSG.format("cookies"))
            self.s.cookies.update(cookies)
        else:
            raise Exception("Insufficient auth data")

    def _create_url(self, *args):
        return self.base_url + "/".join(args)

    def _request(self, method: str, endpoint: str, return_raw: bool = False, **kwargs):
        self.logger.debug(f"{method.capitalize()} data: endpoint={endpoint} and {kwargs}")
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
        self.logger.debug(f"Get paginated data from endpoint={endpoint} and params={params}")
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
