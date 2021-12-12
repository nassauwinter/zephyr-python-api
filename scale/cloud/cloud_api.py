import logging

from ..zephyr_session import ZephyrSession
from scale.cloud.endpoints import (EnvironmentEndpoints, FolderEndpoints, PriorityEndpoints, ProjectEndpoints,
                                   StatusEndpoints, TestCaseEndpoints,TestCycleEndpoints, TestExecutionEndpoints,
                                   TestPlanEndpoints)


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
    def test_executions(self):
        return TestExecutionEndpoints(self.session)

    @property
    def folders(self):
        return FolderEndpoints(self.session)

    @property
    def statuses(self):
        return StatusEndpoints(self.session)

    @property
    def priorities(self):
        return PriorityEndpoints(self.session)

    @property
    def environments(self):
        return EnvironmentEndpoints(self.session)

    @property
    def projects(self):
        return ProjectEndpoints(self.session)
