import logging

from zephyr.squad.zephyr_squad_session import ZephyrSquadSession
from zephyr.squad.server.server_api import ServerApiWrapper
from zephyr.squad.server.actions import ServerActionsWrapper

DEFAULT_BASE_URL = "https://jira.hosted.com/"


class ZephyrSquad:
    """
    Zephyr Squad base object to interact with other objects or raw api by its methods.

    :param base_url: base API url to connect with
    """
    def __init__(self, base_url=None, **kwargs):
        base_url = DEFAULT_BASE_URL if not base_url else base_url
        session = ZephyrSquadSession(base_url=base_url, **kwargs)
        self.api = ServerApiWrapper(session)
        self.actions = ServerActionsWrapper(session)
        self.logger = logging.getLogger(__name__)

    @classmethod
    def server_api(cls, base_url, **kwargs):
        """Alternative constructor for Zephyr Squad Server client"""
        return cls(base_url=base_url, **kwargs)
