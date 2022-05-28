from typing import Union

from ...zephyr_session import ZephyrSession


class TestCycleEndpoints:
    """Api wrapper for "Test Cycle" endpoints"""
    def __init__(self, session: ZephyrSession):
        self.session = session

    def get_all_test_cycles(self, **kwargs):
        return self.session.get_paginated("testcycles", params=kwargs)

    def create_test_cycle(self, project_key: str, name: str, **kwargs):
        json = {"projectKey": project_key,
                "name": name}
        json.update(kwargs)
        return self.session.post("testcycles", json=json)

    def get_test_cycle(self, test_cycle_id_or_key: Union[str, int]):
        return self.session.get(f"testcycles/{test_cycle_id_or_key}")

    def update_test_cycle(self,
                          test_cycle_key: str,
                          test_cycle_id: int,
                          name: str,
                          project_id: str,
                          status_id: str,
                          **kwargs):
        json = {"id": test_cycle_id,
                "key": test_cycle_key,
                "name": name,
                "project": {"id": project_id},
                "status": {"id": status_id}}
        json.update(kwargs)
        return self.session.put(f"testcycles/{test_cycle_key}", json=json)

    def get_links(self, test_cycle_id_or_key: Union[str, int]):
        return self.session.get(f"testcycles/{test_cycle_id_or_key}/links")

    def create_issue_links(self, test_cycle_id_or_key: Union[str, int], issue_id: int):
        json = {"issueId": issue_id}
        return self.session.post(f"testcycles/{test_cycle_id_or_key}/links/issues", json=json)

    def create_web_links(self, test_cycle_id_or_key: Union[str, int], url: str, **kwargs):
        json = {"url": url}
        json.update(kwargs)
        return self.session.post(f"testcycles/{test_cycle_id_or_key}/links/weblinks", json=json)
