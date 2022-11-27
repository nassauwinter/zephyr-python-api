import logging
from urllib.parse import urlparse, parse_qs

from requests import Session


INIT_SESSION_MSG = "Initialize session by {}"


class ZephyrSession:
    """
    Zephyr Scale basic session object.

    :param base_url: url to make requests to
    :param token: auth token
    :param username: username
    :param password: password
    :param cookies: cookie dict
    """
    def __init__(self, base_url, token=None, username=None, password=None, cookies=None):
        self.base_url = base_url
        self._session = Session()
        self.logger = logging.getLogger(__name__)
        if token:
            self.logger.debug(INIT_SESSION_MSG.format("token"))
            self._session.headers.update({"Authorization": f"Bearer {token}"})
        elif username and password:
            self.logger.debug(INIT_SESSION_MSG.format("username and password"))
            self._session.auth = (username, password)
        elif cookies:
            self.logger.debug(INIT_SESSION_MSG.format("cookies"))
            self._session.cookies.update(cookies)
        else:
            raise Exception("Insufficient auth data")

    def _create_url(self, *args):
        """Helper for URL creation"""
        return self.base_url + "/".join(args)

    def _request(self, method: str, endpoint: str, return_raw: bool = False, **kwargs):
        """General request wrapper with logging and handling response"""
        self.logger.debug(f"{method.capitalize()} data: endpoint={endpoint} and {kwargs}")
        url = self._create_url(endpoint)
        response = self._session.request(method=method, url=url, **kwargs)
        if response.status_code < 400:
            if return_raw:
                return response
            if response.text:
                return response.json()
            return ""
        raise Exception(f"Error {response.status_code}. Response: {response.content}")

    def get(self, endpoint: str, params: dict = None, **kwargs):
        """Get request wrapper"""
        return self._request("get", endpoint, params=params, **kwargs)

    def post(self, endpoint: str, json: dict = None, **kwargs):
        """Post request wrapper"""
        return self._request("post", endpoint, json=json, **kwargs)

    def put(self, endpoint: str, json: dict = None, **kwargs):
        """Put request wrapper"""
        return self._request("put", endpoint, json=json, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        """Delete request wrapper"""
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

    def post_file(self, endpoint: str, file_path: str, **kwargs):
        """
        Post wrapper to send a file. Handles single file opening,
        sending its content and closing
        """
        with open(file_path, "rb") as file:
            files = {"file": file}
            return self._request("post", endpoint, files=files, **kwargs)
