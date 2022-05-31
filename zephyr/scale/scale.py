import logging

from zephyr.scale.zephyr_session import ZephyrSession
from zephyr.scale.cloud.cloud_api import CloudApiWrapper


DEFAULT_BASE_URL = "https://api.zephyrscale.smartbear.com/v2/"


class ZephyrScale:
    """
    Zephyr Scale base object to interact with other objects or raw api by its methods

    :param token: Zephyr Scale auth token
    :param base_url: base API url to connect with
    """
    def __init__(self, token, base_url=None):
        base_url = DEFAULT_BASE_URL if not base_url else base_url
        session = ZephyrSession(token=token, base_url=base_url)

        self.api = CloudApiWrapper(session)
        self.logger = logging.getLogger(__name__)
