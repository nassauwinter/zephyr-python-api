from logging import Logger

import pytest

from zephyr.scale.scale import DEFAULT_BASE_URL, ZephyrScale


ZSESSION_PATH = "zephyr.scale.scale.ZephyrScaleSession"
CLOUD_API_WRAP_PATH = "zephyr.scale.scale.CloudApiWrapper"
SERVER_API_WRAP_PATH = "zephyr.scale.scale.ServerApiWrapper"


@pytest.mark.unit
class TestZephyrScale:
    @pytest.mark.parametrize("creation_kwargs, exp_url", [({}, DEFAULT_BASE_URL),
                                                          ({"base_url": DEFAULT_BASE_URL}, DEFAULT_BASE_URL),
                                                          ({"base_url": "test.com"}, "test.com")])
    def test_scale_session_creation(self, creation_kwargs, exp_url, mocker):
        session_mock = mocker.patch(ZSESSION_PATH)
        mocker.patch(CLOUD_API_WRAP_PATH)

        ZephyrScale(**creation_kwargs)

        session_mock.assert_called_once_with(base_url=exp_url)

    @pytest.mark.parametrize("creation_kwargs, api_version", [({}, CLOUD_API_WRAP_PATH),
                                                              ({"api_version": "v2"}, CLOUD_API_WRAP_PATH),
                                                              ({"api_version": "V2"}, CLOUD_API_WRAP_PATH),
                                                              ({"api_version": "v1"}, SERVER_API_WRAP_PATH),
                                                              ({"api_version": "V1"}, SERVER_API_WRAP_PATH)])
    def test_scale_defining_version(self, creation_kwargs, api_version, mocker):
        zsession_mock = mocker.patch(ZSESSION_PATH)
        wrapper_mock = mocker.patch(api_version)

        zephyr = ZephyrScale(**creation_kwargs)

        assert isinstance(zephyr, ZephyrScale), f"Resulted object should be instance of {ZephyrScale}"
        wrapper_mock.assert_called_once_with(zsession_mock())

    @pytest.mark.parametrize("creation_kwargs, api_version", [({"base_url": "test.com"}, SERVER_API_WRAP_PATH)])
    def test_server_cls_method(self, creation_kwargs, api_version, mocker):
        zsession_mock = mocker.patch(ZSESSION_PATH)
        wrapper_mock = mocker.patch(api_version)

        zephyr = ZephyrScale.server_api(**creation_kwargs)
        assert isinstance(zephyr, ZephyrScale), f"Resulted object should be instance of {ZephyrScale}"
        wrapper_mock.assert_called_once_with(zsession_mock())

    @pytest.mark.parametrize("creation_kwargs, exception",
                             [({"api_version": "v"}, ValueError)])
    def test_scale_defining_version_exceptions(self, creation_kwargs, exception, mocker):
        mocker.patch(ZSESSION_PATH)

        with pytest.raises(exception):
            ZephyrScale(**creation_kwargs)

    def test_scale_logger(self, mocker):
        mocker.patch(ZSESSION_PATH)
        mocker.patch(CLOUD_API_WRAP_PATH)

        zephyr = ZephyrScale()

        assert isinstance(zephyr.logger, Logger)
