from zephyr.squad.zephyr_squad_session import ZephyrSquadSession
from zephyr.utils.common import dict_merge
from .paths import ServerPaths as Paths
from .endpoints import UtilResourceEndpoints as UtilResource


class EndpointTemplate:
    """Class with basic constructor for endpoint classes"""
    def __init__(self, session: ZephyrSquadSession):
        self.session = session


class ProjectEndpoints(EndpointTemplate):
    """Api wrapper for "Project" endpoints"""

    def get_project_info(self, project_key):
        """
        Retrieve project information

        :param project_key: Jira project key
        :return: dict with response body
        """
        return self.session.get(Paths.PRJ_ID.format(project_key))

    def get_project_versions_by_key(self, project_key):
        """
        Retrieve all project versions (releases) by project key using Jira API

        :param project_key: Jira project key
        :return: list of dict for each version
        """
        return self.session.get(Paths.PRJ_VERSIONS_BY_KEY.format(project_key))


class TestCaseEndpoints(EndpointTemplate):
    """Api wrapper for "Test Case" endpoints"""

    def get_test_case(self, test_case_key, **params):
        """Retrieve the Test Case matching the given key"""
        return self.session.get(Paths.CASE_KEY.format(test_case_key),
                                params=params)

    def create_test_case(self, project_id, summary, data):
        """
        Creates a new Test Case based on a minimum required fields.

        (https://support.smartbear.com/zephyr-squad-server/docs/api/how-to/create-tests.html)
        See Zephyr Squad Test Case creation documentation to better understand what can be
        modified.
        """
        case_type = UtilResource(self.session).get_zephyr_issue_type()["testcaseIssueTypeId"]
        json = {
            "fields": {
                "project": {
                    "id": project_id
                },
                'issuetype': {
                    'id': case_type
                },
                "summary": summary,
            }
        }
        merged_json = dict_merge(data, json)
        return self.session.post(Paths.CASE, json=merged_json)
