import logging

from zephyr.squad.zephyr_squad_session import ZephyrSquadSession
from zephyr.squad.server import endpoints


# pylint: disable=missing-function-docstring
class ServerActionsWrapper:
    """Zephyr Squad Server Actions wrapper"""
    def __init__(self, session: ZephyrSquadSession):
        self.session = session
        self.logger = logging.getLogger(__name__)

    @property
    def project(self):
        return endpoints.ProjectEndpoints(self.session)

    @property
    def test_cases(self):
        return endpoints.TestCaseEndpoints(self.session)
