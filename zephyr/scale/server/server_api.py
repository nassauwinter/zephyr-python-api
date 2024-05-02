"""
A module with the Zephyr Scale Server Api wrapper class.
"""
import logging

from zephyr.scale.zephyr_session import ZephyrSession
from zephyr.scale.server import endpoints


class ServerApiWrapper:
    """
    Zephyr Scale Server Api wrapper class. It contains API endpoint wrappers for the Zephyr Scale
    Server/Datacenter. The wrappers are grouped by the entity they are related to.
    These wrapper groups are represented by the properties of the class.

    For more details on the API endpoints see docs:
    https://support.smartbear.com/zephyr-scale-server/api-docs/v1/

    :param session: ZephyrSession object with auth credentials
    """
    def __init__(self, session: ZephyrSession):
        self.session = session
        self.logger = logging.getLogger(__name__)

    @property
    def attachments(self):
        """Attachment endpoints."""
        return endpoints.AttachmentEndpoints(self.session)

    @property
    def automation(self):
        """Automation endpoints."""
        return endpoints.AutomationEndpoints(self.session)

    @property
    def custom_field(self):
        """Custom field endpoints."""
        return endpoints.CustomFieldEndpoints(self.session)

    @property
    def delete_execution(self):
        """Delete execution endpoints."""
        return endpoints.DeleteExecutionEndpoints(self.session)

    @property
    def environment(self):
        """Environment endpoints."""
        return endpoints.EnvironmentEndpoints(self.session)

    @property
    def folder(self):
        """Folder endpoints."""
        return endpoints.FolderEndpoints(self.session)

    @property
    def issue_link(self):
        """Issue link endpoints."""
        return endpoints.IssueLinkEndpoints(self.session)

    @property
    def project(self):
        """Project endpoints."""
        return endpoints.ProjectEndpoints(self.session)

    @property
    def test_cases(self):
        """Test case endpoints."""
        return endpoints.TestCaseEndpoints(self.session)

    @property
    def test_plans(self):
        """Test plan endpoints."""
        return endpoints.TestPlanEndpoints(self.session)

    @property
    def test_results(self):
        """Test result endpoints."""
        return endpoints.TestResultEndpoints(self.session)

    @property
    def test_runs(self):
        """Test run endpoints."""
        return endpoints.TestRunEndpoints(self.session)
