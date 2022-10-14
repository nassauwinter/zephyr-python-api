import logging

from zephyr.scale.zephyr_session import ZephyrSession
from zephyr.scale.server import endpoints


class ServerApiWrapper:
    """Zephyr Scale Server Api wrapper"""
    def __init__(self, session: ZephyrSession):
        self.session = session
        self.logger = logging.getLogger(__name__)

    @property
    def attachments(self):
        return endpoints.AttachmentEndpoints(self.session)

    @property
    def automation(self):
        return endpoints.AutomationEndpoints(self.session)

    @property
    def custom_field(self):
        return endpoints.CustomFieldEndpoints(self.session)

    @property
    def delete_execution(self):
        return endpoints.DeleteExecutionEndpoints(self.session)

    @property
    def environment(self):
        return endpoints.EnvironmentEndpoints(self.session)

    @property
    def folder(self):
        return endpoints.FolderEndpoints(self.session)

    @property
    def issue_link(self):
        return endpoints.IssueLinkEndpoints(self.session)

    @property
    def project(self):
        return endpoints.ProjectEndpoints(self.session)

    @property
    def test_cases(self):
        return endpoints.TestCaseEndpoints(self.session)

    @property
    def test_plans(self):
        return endpoints.TestPlanEndpoints(self.session)

    @property
    def test_results(self):
        return endpoints.TestResultEndpoints(self.session)

    @property
    def test_runs(self):
        return endpoints.TestRunEndpoints(self.session)
