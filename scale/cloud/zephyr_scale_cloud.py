import logging

from scale.zephyr_session import ZephyrSession
from scale.cloud.cloud_api import CloudApiWrapper


class ZephyrScaleCloud:
    """Zephyr Scale Cloud base object to interact with other objects or raw api by its methods"""
    def __init__(self, session: ZephyrSession):
        self.api = CloudApiWrapper(session)
        self.logger = self.logger = logging.getLogger(__name__)
