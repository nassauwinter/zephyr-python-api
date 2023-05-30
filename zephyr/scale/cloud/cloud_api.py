import logging
from zephyr.scale.zephyr_scale_session import ZephyrScaleSession
from zephyr.scale.cloud.endpoints import (AutomationEndpoints,
                                          EnvironmentEndpoints,
                                          FolderEndpoints,
                                          HealthcheckEndpoints,
                                          LinkEndpoints,
                                          PriorityEndpoints,
                                          ProjectEndpoints,
                                          StatusEndpoints,
                                          TestCaseEndpoints,
                                          TestCycleEndpoints,
                                          TestExecutionEndpoints,
                                          TestPlanEndpoints)


# pylint: disable=missing-function-docstring
class CloudApiWrapper:
    """Zephyr Scale Cloud Api wrapper. Contains wrappers by sections."""
    def __init__(self, session: ZephyrScaleSession):
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

    @property
    def links(self):
        return LinkEndpoints(self.session)

    @property
    def automations(self):
        return AutomationEndpoints(self.session)

    @property
    def healthcheck(self):
        return HealthcheckEndpoints(self.session)
