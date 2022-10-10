import logging

from zephyr.scale.zephyr_session import ZephyrSession
from zephyr.scale.server.enpoints import (TestCaseEndpoints,
                                          TestPlanEndpoints,
                                          TestRunEndpoints)


class ServerApiWrapper:
    """Zephyr Scale Server Api wrapper"""
    def __init__(self, session: ZephyrSession):
        self.session = session
        self.logger = logging.getLogger(__name__)

    @property
    def test_cases(self):
        return TestCaseEndpoints(self.session)

    @property
    def test_runs(self):
        return TestRunEndpoints(self.session)

    @property
    def test_plans(self):
        return TestPlanEndpoints(self.session)
