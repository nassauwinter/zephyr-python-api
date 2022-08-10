from typing import Union

from ...zephyr_session import ZephyrSession


class TestExecutionEndpoints:
    """Api wrapper for "Test Execution" endpoints"""
    def __init__(self, session: ZephyrSession):
        self.session = session

    def get_test_executions(self, **kwargs):
        """
        Returns all test executions. Query parameters can be used to filter
        by project and folder
        """
        return self.session.get_paginated("testexecutions", params=kwargs)

    def create_test_execution(self,
                              project_key: str,
                              test_case_key: str,
                              test_cycle_key: str,
                              status_name: str,
                              **kwargs):
        """
        Creates a test execution. All required test execution custom fields
        should be present in the request
        """
        json = {"projectKey": project_key,
                "testCaseKey": test_case_key,
                "testCycleKey": test_cycle_key,
                "statusName": status_name}
        json.update(kwargs)
        return self.session.post("testexecutions", json=json)

    def get_test_execution(self, test_execution_id_or_key: Union[str, int], **kwargs):
        """Returns a test execution for the given ID"""
        return self.session.get(f"testexecutions/{test_execution_id_or_key}", params=kwargs)

    def get_links(self, test_execution_id_or_key: Union[str, int]):
        """Returns links for a test execution with specified ID"""
        return self.session.get(f"testexecutions/{test_execution_id_or_key}/links")

    def create_issue_links(self, test_execution_id_or_key: Union[str, int], issue_id: int):
        """Creates a link between a test execution and a Jira issue"""
        return self.session.post(f"testexecutions/{test_execution_id_or_key}/links",
                                 json={"issueId": issue_id})
