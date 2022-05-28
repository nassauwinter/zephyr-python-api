from ...zephyr_session import ZephyrSession


class TestCaseEndpoints:
    """Api wrapper for "Test Case" endpoints"""
    def __init__(self, session: ZephyrSession):
        self.session = session

    def get_test_cases(self, **kwargs):
        """Retrieves all test cases. Query parameters can be used to filter the results.

        Keyword arguments:
        :keyword projectKey: Jira project key filter
        :keyword folderId: Folder ID filter
        :keyword maxResults: A hint as to the maximum number of results to return in each call
        :keyword startAt: Zero-indexed starting position. Should be a multiple of maxResults
        :return: dict with response body
        """
        return self.session.get_paginated("testcases", params=kwargs)

    def create_test_case(self, project_key: str, name: str, **kwargs):
        """Creates a test case. Fields priorityName and statusName will be set to default values if not informed.
        Default values are usually “Normal” for priorityName and “Draft” for statusName. All required test case custom
        fields should be present in the request.

        :param project_key: Jira project key
        :param name: test case name

        Keyword arguments:
        :keyword objective: A description of the objective
        :keyword precondition: Any conditions that need to be met
        :keyword estimatedTime: Estimated duration in milliseconds
        :keyword componentId: ID of a component from Jira
        :keyword priorityName: The priority name
        :keyword statusName: The status name
        :keyword folderId: ID of a folder to place the entity within
        :keyword ownerId: Atlassian Account ID of the Jira user
        :keyword labels: Array of labels associated to this entity
        :return: dict with response body
        """
        json = {"projectKey": project_key,
                "name": name}
        json.update(kwargs)
        return self.session.post("testcases", json=json)

    def get_test_case(self, test_case_key: str):
        """Returns a test case for the given key

        :param test_case_key: The key of the test case
        :return: dict with response body
        """
        return self.session.get(f"testcases/{test_case_key}")

    def update_test_case(self,
                         test_case_key: str,
                         test_case_id: int,
                         name: str,
                         project_id: int,
                         priority_id: int,
                         status_id: int,
                         **kwargs):
        """Updates an existing test case.

        :param test_case_key: The key of the test case
        :param test_case_id: integer id of the test
        :param name: test case nae
        :param project_id: project id
        :param priority_id: priority id
        :param status_id: status id

        :return: dict with response body
        """
        json = {"id": test_case_id,
                "key": test_case_key,
                "name": name,
                "project": {"id": project_id},
                "priority": {"id": priority_id},
                "status": {"id": status_id}}
        json.update(kwargs)
        return self.session.put(f"testcases/{test_case_key}", json=json)

    def get_links(self, test_case_key: str):
        return self.session.get(f"testcases/{test_case_key}/links")

    def create_issue_links(self, test_case_key: str, issue_id: int):
        json = {"issueId": issue_id}
        return self.session.post(f"testcases/{test_case_key}/links/issues", json=json)

    def create_web_links(self, test_case_key: str, url: str, **kwargs):
        json = {"url": url}
        json.update(kwargs)
        return self.session.post(f"testcases/{test_case_key}/links/weblinks", json=json)

    def get_versions(self, test_case_key: str, **kwargs):
        return self.session.get_paginated(f"testcases/{test_case_key}/versions", params=kwargs)

    def get_version(self, test_case_key: str, version: str):
        return self.session.get(f"testcases/{test_case_key}/versions/{version}")

    def get_test_script(self, test_case_key: str):
        return self.session.get(f"testcases/{test_case_key}/testscript")

    def create_test_script(self, test_case_key: str, script_type: str, text: str):
        json = {"type": script_type, "text": text}
        return self.session.post(f"testcases/{test_case_key}/testscript", json=json)

    def get_test_steps(self, test_case_key: str, **kwargs):
        return self.session.get_paginated(f"testcases/{test_case_key}/teststeps", params=kwargs)

    def post_test_steps(self, test_case_key: str, mode: str, items: list):
        json = {"mode": mode,
                "items": items}
        return self.session.post(f"testcases/{test_case_key}/teststeps", json=json)
