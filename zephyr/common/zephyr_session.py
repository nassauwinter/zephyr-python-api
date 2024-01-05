import logging

from requests import HTTPError, Session


INIT_SESSION_MSG = "Initialize session by {}"


class InvalidAuthData(Exception):
    """Invalid authentication data provided"""


class ZephyrSession:
    """
    Zephyr basic session object.

    :param base_url: url to make requests to
    :param token: auth token
    :param username: username
    :param password: password
    :param cookies: cookie dict

    :keyword session_attrs: a dict with session attrs to be set as keys and their values
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
        raise HTTPError(f"Error {response.status_code}. Response: {response.content}")

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
