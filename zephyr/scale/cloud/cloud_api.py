"""
A module with the Zephyr Scale Cloud Api wrapper class.
"""
import logging

from zephyr.scale.zephyr_session import ZephyrSession
from zephyr.scale.cloud import endpoints


# pylint: disable=missing-function-docstring
class CloudApiWrapper:
    """Zephyr Scale Cloud Api wrapper. Contains wrappers by sections."""
    def __init__(self, session: ZephyrSession):
        self.session = session
        self.logger = logging.getLogger(__name__)

    @property
    def test_cases(self):
        return endpoints.TestCaseEndpoints(self.session)

    @property
    def test_cycles(self):
        return endpoints.TestCycleEndpoints(self.session)

    @property
    def test_plans(self):
        return endpoints.TestPlanEndpoints(self.session)

    @property
    def test_executions(self):
        return endpoints.TestExecutionEndpoints(self.session)

    @property
    def folders(self):
        return endpoints.FolderEndpoints(self.session)

    @property
    def statuses(self):
        return endpoints.StatusEndpoints(self.session)

    @property
    def priorities(self):
        return endpoints.PriorityEndpoints(self.session)

    @property
    def environments(self):
        return endpoints.EnvironmentEndpoints(self.session)

    @property
    def projects(self):
        return endpoints.ProjectEndpoints(self.session)

    @property
    def links(self):
        return endpoints.LinkEndpoints(self.session)

    @property
    def automations(self):
        return endpoints.AutomationEndpoints(self.session)

    @property
    def healthcheck(self):
        return endpoints.HealthcheckEndpoints(self.session)
