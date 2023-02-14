import pytest
from requests import Session

from zephyr.scale.scale import DEFAULT_BASE_URL, ZephyrSession
from zephyr.scale.zephyr_session import INIT_SESSION_MSG, InvalidAuthData

REQUESTS_SESSION_PATH = "requests.sessions.Session"
GETLOGGER_PATH = "logging.getLogger"
LOGGER_DEBUG_PATH = "logging.Logger.debug"


@pytest.mark.unit
class TestZephyrSession:
    def test_creation(self, mocker):
        """Tests basic creation logic"""
        logger_mock = mocker.patch(GETLOGGER_PATH)

        zsession = ZephyrSession(DEFAULT_BASE_URL, token="token_test")

        assert zsession.base_url == DEFAULT_BASE_URL, (f"Attribute base_url expected to be {DEFAULT_BASE_URL}, "
                                                       f"not {zsession.base_url}")
        assert isinstance(zsession._session, Session)
        logger_mock.assert_called_with("zephyr.scale.zephyr_session")

    def test_token_auth(self, mocker):
        """Test token auth"""
        token = "test_token"
        logger_mock = mocker.patch(LOGGER_DEBUG_PATH)

        zsession = ZephyrSession(DEFAULT_BASE_URL, token=token)

        logger_mock.assert_called_with(INIT_SESSION_MSG.format("token"))
        assert f"Bearer {token}" == zsession._session.headers.get("Authorization")

    def test_credentials_auth(self, mocker):
        """Test auth with username and password"""
        username = "usertest"
        password = "pwdtest"
        logger_mock = mocker.patch(LOGGER_DEBUG_PATH)

        zsession = ZephyrSession(DEFAULT_BASE_URL, username=username, password=password)

        logger_mock.assert_called_with(INIT_SESSION_MSG.format("username and password"))
        assert (username, password) == zsession._session.auth

    def test_cookie_auth(self, mocker):
        """Test auth with cookie dict"""
        test_cookie = {"cookies": {"cookie.token": "cookie_test"}}
        logger_mock = mocker.patch(LOGGER_DEBUG_PATH)

        zsession = ZephyrSession(DEFAULT_BASE_URL, cookies=test_cookie)

        logger_mock.assert_called_with(INIT_SESSION_MSG.format("cookies"))
        assert test_cookie['cookies'] in zsession._session.cookies.values()

    @pytest.mark.parametrize("auth_data, exception", [(dict(), InvalidAuthData),
                                                      ({"username": "user"}, InvalidAuthData),
                                                      ({"password": "pwd"}, InvalidAuthData)])
    def test_auth_exception(self, auth_data, exception):
        """Test exceptions on auth"""
        with pytest.raises(exception):
            ZephyrSession(DEFAULT_BASE_URL, **auth_data)

    @pytest.mark.parametrize("creation_kwargs",
                             [{"token": "token_test",
                               "session_attrs": {'verify': False, "max_redirects": 333}}])
    def test_requests_session_attrs(self, creation_kwargs, mocker):
        """The test checks ZephyrScale (not) provided with "session_attrs"."""
        logger_mock = mocker.patch(LOGGER_DEBUG_PATH)
        session_attrs = creation_kwargs.get('session_attrs')

        zsession = ZephyrSession(DEFAULT_BASE_URL, **creation_kwargs)

        logger_mock.assert_called_with(
            f"Modify requests session object with {session_attrs}")

        for attrib, value in session_attrs.items():
            actual = getattr(zsession._session, attrib)
            assert actual == session_attrs[attrib], (f"Request session attr {attrib} is {actual}, "
                                                     f"but expected{session_attrs[attrib]}")

    @pytest.mark.skip
    def test_crud_request(self):
        """Test GET, POST, PUT, DELETE requests"""
        pass

    @pytest.mark.skip
    def test_get_paginated(self):
        """Test paginated request"""
        pass

    @pytest.mark.skip
    def test_post_file(self):
        """Test Post file wrapper"""
        pass
