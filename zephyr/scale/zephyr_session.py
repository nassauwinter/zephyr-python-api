"""
A module for Zephyr Scale session object.
"""
import logging
from urllib.parse import urlparse, parse_qs

from requests import HTTPError, Session


INIT_SESSION_MSG = "Initialize session by {}"


class InvalidAuthData(Exception):
    """Raised when Invalid authentication data provided."""


class ZephyrSession:
    """
    Zephyr Scale basic session object. The authentication and response handling logic
    is placed here.

    :param base_url: url to make requests to
    :param token: auth token
    :param username: username
    :param password: password
    :param cookies: cookie dict

    :param keyword session_attrs: a dict with session attrs to be set as keys and their values
    """
    def __init__(self, base_url, token=None, username=None, password=None, cookies=None, **kwargs):
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
            raise InvalidAuthData("Insufficient auth data")

        if kwargs.get("session_attrs"):
            self._modify_session(**kwargs.get("session_attrs"))

    def _create_url(self, *args):
        """Helper for URL creation"""
        return self.base_url + "/".join(args)

    def _modify_session(self, **kwargs):
        """Modify requests session with extra arguments"""
        self.logger.debug(f"Modify requests session object with {kwargs}")
        for session_attr, value in kwargs.items():
            setattr(self._session, session_attr, value)

    def _request(self, method: str, endpoint: str, return_raw: bool = False, **kwargs):
        """
        General request wrapper with logging and handling response

        :param method: request method
        :param endpoint: endpoint to make request to
        :param return_raw: whether to return raw response or not

        :raises: HTTPError if response status code is 400 or higher

        :return: response json, empty str or raw response
        """
        self.logger.debug(f"{method.capitalize()} data: endpoint={endpoint} and {kwargs}")
        url = self._create_url(endpoint)
        response = self._session.request(method=method, url=url, **kwargs)
        if response.status_code < 400:
            if return_raw:
                return response
            if response.text:
                return response.json()
            return ""
        raise HTTPError(f"Error {response.status_code}. Response: {response.content}")

    def get(self, endpoint: str, params: dict = None, **kwargs):
        """
        Get request wrapper.

        :param endpoint: endpoint to make request to
        :param params: dict with params to be passed to request

        :return: response json, empty str or raw response
        """
        return self._request("get", endpoint, params=params, **kwargs)

    def post(self, endpoint: str, json: dict = None, **kwargs):
        """
        Post request wrapper.

        :param endpoint: endpoint to make request to
        :param json: json to be passed to request

        :return: response json, empty str or raw response
        """
        return self._request("post", endpoint, json=json, **kwargs)

    def put(self, endpoint: str, json: dict = None, **kwargs):
        """
        Put request wrapper

        :param endpoint: endpoint to make request to
        :param json: json to be passed to request

        :return: response json, empty str or raw response
        """
        return self._request("put", endpoint, json=json, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        """
        Delete request wrapper.

        :param endpoint: endpoint to make request to

        :return: response json, empty str or raw response
        """
        return self._request("delete", endpoint, **kwargs)

    def get_paginated(self, endpoint, params=None):
        """
        Get request wrapper for getting paginated data. Yields values from multiple get requests
        responses.

        :param endpoint: endpoint to make request to
        :param params: dict with params to be passed to request

        :return: generator with values from responses
        """
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

    def post_file(self, endpoint: str, file_path: str, to_files=None, **kwargs):
        """
        Post wrapper to send a file. Handles single file opening, sending its content and closing.

        :param endpoint: endpoint to make request to
        :param file_path: path to file to be sent
        :param to_files: dict with files to be sent along with the main file

        :return: response json, empty str or raw response
        """
        with open(file_path, "rb") as file:
            files = {"file": file}

            if to_files:
                files.update(to_files)

            return self._request("post", endpoint, files=files, **kwargs)
