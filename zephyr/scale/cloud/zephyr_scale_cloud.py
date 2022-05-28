import logging

from zephyr.scale.zephyr_session import ZephyrSession
from zephyr.scale.cloud import CloudApiWrapper


class ZephyrScaleCloud:
    """Zephyr Scale Cloud base object to interact with other objects or raw api by its methods"""
    def __init__(self, session: ZephyrSession):
        self.api = CloudApiWrapper(session)
        self.logger = self.logger = logging.getLogger(__name__)
