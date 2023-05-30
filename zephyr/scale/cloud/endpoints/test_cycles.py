from typing import Union

from zephyr.scale.zephyr_scale_session import ZephyrScaleSession


class TestCycleEndpoints:
    """Api wrapper for "Test Cycle" endpoints"""
    def __init__(self, session: ZephyrScaleSession):
        self.session = session

    def get_all_test_cycles(self, **kwargs):
        """
        Returns all test cycles. Query parameters can be used to filter
        by project and folder
        """
        return self.session.get_paginated("testcycles", params=kwargs)

    def create_test_cycle(self, project_key: str, name: str, **kwargs):
        """
        Creates a Test Cycle. All required test cycle custom fields
        should be present in the request
        """
        json = {"projectKey": project_key,
                "name": name}
        json.update(kwargs)
        return self.session.post("testcycles", json=json)

    def get_test_cycle(self, test_cycle_id_or_key: Union[str, int]):
        """Returns a test cycle for the given key"""
        return self.session.get(f"testcycles/{test_cycle_id_or_key}")

    def update_test_cycle(self,
                          test_cycle_key: str,
                          test_cycle_id: int,
                          name: str,
                          project_id: str,
                          status_id: str,
                          **kwargs):
        """
        Updates an existing test cycle. If the project has test cycle
        custom fields, all custom fields should be present in the request.
        To leave any of them blank, please set them null
        if they are not required custom fields.
        """
        json = {"id": test_cycle_id,
                "key": test_cycle_key,
                "name": name,
                "project": {"id": project_id},
                "status": {"id": status_id}}
        json.update(kwargs)
        return self.session.put(f"testcycles/{test_cycle_key}", json=json)

    def get_links(self, test_cycle_id_or_key: Union[str, int]):
        """Returns links for a test cycle with specified key"""
        return self.session.get(f"testcycles/{test_cycle_id_or_key}/links")

    def create_issue_links(self, test_cycle_id_or_key: Union[str, int], issue_id: int):
        """Creates a link between a test cycle and a Jira issue"""
        json = {"issueId": issue_id}
        return self.session.post(f"testcycles/{test_cycle_id_or_key}/links/issues", json=json)

    def create_web_links(self, test_cycle_id_or_key: Union[str, int], url: str, **kwargs):
        """Creates a link between a test cycle and a generic URL"""
        json = {"url": url}
        json.update(kwargs)
        return self.session.post(f"testcycles/{test_cycle_id_or_key}/links/weblinks", json=json)
