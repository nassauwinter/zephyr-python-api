import logging

from zephyr.scale.zephyr_session import ZephyrSession
from zephyr.scale.cloud.cloud_api import CloudApiWrapper


DEFAULT_BASE_URL = "https://api.zephyrscale.smartbear.com/v2/"

API_V2 = "v2"
API_V1 = "v1"


class ZephyrScale:
    """
    Zephyr Scale base object to interact with other objects or raw api by its methods.

    NOTE: Cloud API accepts only token auth, whereas Server API works with Jira auth methods.

    :param base_url: base API url to connect with
    :param api_version: 'v2' for Cloud and 'v1' for Server
    """
    def __init__(self, base_url=None, api_version=API_V2, **kwargs):
        base_url = DEFAULT_BASE_URL if not base_url else base_url
        session = ZephyrSession(base_url=base_url, **kwargs)

        if api_version == API_V2:
            self.api = CloudApiWrapper(session)
        elif api_version == API_V1:
            raise NotImplemented
        else:
            raise Exception("API version should be either 'v1' (Server) or 'v2' (Cloud)")
        self.logger = logging.getLogger(__name__)
