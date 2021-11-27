import logging

from ..zephyr_session import ZephyrSession
from .endpoints.test_cases import TestCaseEndpoints
from .endpoints.projects import ProjectEndpoints
from .endpoints.test_cycles import TestCycleEndpoints
from .endpoints.test_plans import TestPlanEndpoints


class CloudApiWrapper(object):
    """Zephyr Scale Cloud Api wrapper"""
    def __init__(self, session: ZephyrSession):
        self.session = session
        self.logger = logging.getLogger(__name__)

    @property
    def test_cases(self):
        return TestCaseEndpoints(self.session)

    @property
    def test_cycles(self):
        return TestCycleEndpoints(self.session)

    @property
    def test_plans(self):
        return TestPlanEndpoints(self.session)

    @property
    def projects(self):
        return ProjectEndpoints(self.session)
