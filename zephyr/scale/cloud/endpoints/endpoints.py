from json import dumps
from typing import Union

from ...zephyr_session import EndpointTemplate
from .paths import CloudPaths as Paths


class TestCaseEndpoints(EndpointTemplate):
    """
    Api wrapper for "Test Case" endpoints

    Details: https://support.smartbear.com/zephyr-scale-cloud/api-docs/#tag/Test-Cases
    """

    def get_test_cases(self, **kwargs):
        """Retrieves all test cases. Query parameters can be used to filter the results.

        Keyword arguments:
        :keyword projectKey: Jira project key filter
        :keyword folderId: Folder ID filter
        :keyword maxResults: A hint as to the maximum number of results to return in each call
        :keyword startAt: Zero-indexed starting position. Should be a multiple of maxResults
        :return: dict with response body
        """
        return self.session.get_paginated(Paths.CASES, params=kwargs)

    def create_test_case(self, project_key: str, name: str, **kwargs):
        """Creates a test case. Fields priorityName and statusName will be set to
        default values if not informed. Default values are usually “Normal”
        for priorityName and “Draft” for statusName. All required test case custom
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
        return self.session.post(Paths.CASES, json=json)

    def get_test_case(self, test_case_key: str):
        """Returns a test case for the given key

        :param test_case_key: The key of the test case
        :return: dict with response body
        """
        return self.session.get(Paths.CASE_KEY.format(test_case_key))

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
        return self.session.put(Paths.CASE_KEY.format(test_case_key),
                                json=json)

    def get_links(self, test_case_key: str):
        """Returns links for a test case with specified key"""
        return self.session.get(Paths.CASE_LINKS.format(test_case_key))

    def create_issue_links(self, test_case_key: str, issue_id: int):
        """Creates a link between a test case and a Jira issue"""
        json = {"issueId": issue_id}
        return self.session.post(Paths.CASE_ISSUES.format(test_case_key),
                                 json=json)

    def create_web_links(self, test_case_key: str, url: str, **kwargs):
        """Creates a link between a test case and a generic URL"""
        json = {"url": url}
        json.update(kwargs)
        return self.session.post(Paths.CASE_WEBLINKS.format(test_case_key),
                                 json=json)

    def get_versions(self, test_case_key: str, **kwargs):
        """
        Returns all test case versions for a test case with specified key.
        Response is ordered by most recent first
        """
        return self.session.get_paginated(Paths.CASE_VERS.format(test_case_key),
                                          params=kwargs)

    def get_version(self, test_case_key: str, version: str):
        """Retrieves a specific version of a test case"""
        return self.session.get(Paths.CASE_VER.format(test_case_key, version))

    def get_test_script(self, test_case_key: str):
        """Returns the test script for the given test case"""
        return self.session.get(Paths.CASE_SCRIPT.format(test_case_key))

    def create_test_script(self, test_case_key: str, script_type: str, text: str):
        """
        Creates or updates the test script for a test case. If the test case currently
        has a sequence of test steps assigned to it, these will be implicitly removed.
        """
        json = {"type": script_type, "text": text}
        return self.session.post(Paths.CASE_SCRIPT.format(test_case_key),
                                 json=json)

    def get_test_steps(self, test_case_key: str, **kwargs):
        """
        Returns the test steps for the given test case. Provides a paged response,
        with 100 items per page.
        """
        return self.session.get_paginated(Paths.CASE_STEPS.format(test_case_key),
                                          params=kwargs)

    def post_test_steps(self, test_case_key: str, mode: str, items: list):
        """
        Assigns a series of test steps to a test case, appending them to any existing
        sequence of test steps. A maximum of 100 steps can be posted per request. Consumers
        should not attempt to parallelize this operation, as the order of the steps is defined
        by the input order. If this endpoint is called on a test case that already has
        a plain text or BDD test script, that test script will implicitly be removed.
        All required step custom fields should be present in the request.
        """
        json = {"mode": mode,
                "items": items}
        return self.session.post(Paths.CASE_STEPS.format(test_case_key),
                                 json=json)


class TestCycleEndpoints(EndpointTemplate):
    """
    Api wrapper for "Test Cycle" endpoints

    Details: https://support.smartbear.com/zephyr-scale-cloud/api-docs/#tag/Test-Cycles
    """

    def get_test_cycles(self, **kwargs):
        """Retrieves all test cycles. Query parameters can be used to filter the results.

        Keyword arguments:
        :keyword projectKey: Jira project key filter
        :keyword folderId: Folder ID filter
        :keyword maxResults: A hint as to the maximum number of results to return in each call
        :keyword startAt: Zero-indexed starting position. Should be a multiple of maxResults
        :return: dict with response body
        """
        return self.session.get_paginated(Paths.CYCLES, params=kwargs)

    def create_test_cycle(self, project_key: str, name: str, **kwargs):
        """Creates a test cycle. All required test cycle custom fields should be present in the request.

        :param project_key: Jira project key
        :param name: test cycle name
        :return: dict with response body
        """
        json = {"projectKey": project_key,
                "name": name}
        json.update(kwargs)
        return self.session.post(Paths.CYCLES, json=json)

    def get_test_cycle(self, test_cycle_id_or_key: Union[str, int]):
        """
        Returns a test cycle for the given key

        :pqram test_cycle_id_or_key: The ID or key of the test cycle
        :return: dict with response body
        """
        return self.session.get(Paths.CYCLE_KEY.format(test_cycle_id_or_key))

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

        :param test_cycle_key: The ID or key of the test cycle
        :param test_cycle_id: integer id of the test cycle
        :param name: Name of the Test Cycle
        :param project_id: project id
        :param status_id: status id
        :return: dict with response body
        """
        json = {"id": test_cycle_id,
                "key": test_cycle_key,
                "name": name,
                "project": {"id": project_id},
                "status": {"id": status_id}}
        json.update(kwargs)
        return self.session.put(Paths.CYCLE_KEY, json=json)

    def get_links(self, test_cycle_id_or_key: Union[str, int]):
        """
        Returns links for a test cycle with specified key

        :param test_cycle_id_or_key: The ID or key of the test cycle
        """
        return self.session.get(Paths.CYCLE_LINKS.format(test_cycle_id_or_key))

    def create_issue_links(self, test_cycle_id_or_key: Union[str, int], issue_id: int):
        """
        Creates a link between a test cycle and a Jira issue

        :param test_cycle_id_or_key: The ID or key of the test cycle
        :param issue_id: The id of the issue
        :return: dict with response body
        """
        json = {"issueId": issue_id}
        return self.session.post(Paths.CYCLE_ISSUES.format(test_cycle_id_or_key),
                                 json=json)

    def create_web_links(self, test_cycle_id_or_key: Union[str, int], url: str, **kwargs):
        """
        Creates a link between a test cycle and a generic URL

        :param test_cycle_id_or_key: The ID or key of the test cycle
        :param url: The web link URL
        :return: dict with response body
        """
        json = {"url": url}
        json.update(kwargs)
        return self.session.post(Paths.CYCLE_WEBLINKS.format(test_cycle_id_or_key),
                                 json=json)


class TestPlanEndpoints(EndpointTemplate):
    """Api wrapper for "Test Plan" endpoints"""

    def get_test_plans(self, **kwargs):
        """Retrieves all test plans. Query parameters can be used to filter the results.

        Keyword arguments:
        :keyword projectKey: Jira project key filter
        :keyword maxResults: A hint as to the maximum number of results to return in each call
        :keyword startAt: Zero-indexed starting position. Should be a multiple of maxResults
        :return: dict with response body
        """
        return self.session.get_paginated(Paths.PLANS, params=kwargs)

    def create_test_plan(self, project_key: str, name: str, **kwargs):
        """Creates a test plan. All required test plan custom fields should be present in the request.

        :param project_key: Jira project key
        :param name: test plan name
        :return: dict with response body
        """
        json = {"projectKey": project_key,
                "name": name}
        json.update(kwargs)
        return self.session.post(Paths.PLANS, json=json)

    def get_test_plan(self, test_plan_key: Union[str, int]):
        """
        Returns a test plan for the given id or key.

        :param test_plan_key: The ID or key of the test plan. Test plan keys are of the format [A-Z]+-P[0-9]+
        :return: dict with response body
        """
        return self.session.get(Paths.PLAN_KEY.format(test_plan_key))

    def create_web_links(self, test_plan_key: Union[str, int], url: str, description: str):
        """
        Creates a link between a test plan and a generic URL.

        :param test_plan_key: The ID or key of the test plan. Test plan keys are of the format [A-Z]+-P[0-9]+
        :param url: The web link URL
        :param description: The link description
        :return: dict with response body
        """
        json = {"url": url, "description": description}
        return self.session.post(Paths.PLAN_WEBLINKS.format(test_plan_key),
                                 json=json)

    def create_issue_link(self, test_plan_key: Union[str, int], issue_id: int):
        """
        Creates a link between a test plan and a Jira issue.

        :param test_plan_key: The ID or key of the test plan. Test plan keys are of the format [A-Z]+-P[0-9]+
        :param issue_id: The issue ID
        :return: dict with response body
        """
        return self.session.post(Paths.PLAN_ISSUES.format(test_plan_key),
                                 json={"issueId": issue_id})

    def create_test_cycle_link(self, test_plan_key: Union[str, int], test_cycle_id: int):
        """
        Creates a link between a test plan and a test cycle.

        :param test_plan_key: The ID or key of the test plan. Test plan keys are of the format [A-Z]+-P[0-9]+
        :param test_cycle_id: The ID or key of the test cycle. Test cycle keys are of the format [A-Z]+-R[0-9]+
        :return: dict with response body
        """
        return self.session.post(Paths.PLAN_CYCLES.format(test_plan_key),
                                 json={"testCycleIdOrKey": test_cycle_id})


class TestExecutionEndpoints(EndpointTemplate):
    """Api wrapper for "Test Execution" endpoints"""

    def get_test_executions(self, **kwargs):
        """
        Returns all test executions. Query parameters can be used to filter
        by project and folder
        """
        return self.session.get_paginated(Paths.EXECUTIONS, params=kwargs)

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
        return self.session.post(Paths.EXECUTIONS, json=json)

    def get_test_execution(self, test_execution_id_or_key: Union[str, int], **kwargs):
        """
        Returns a test execution for the given ID

        :param test_execution_id_or_key: The ID or key of the test execution.
        Test execution keys are of the format [A-Z]+-E[0-9]+
        :return: dict with response body
        """
        return self.session.get(Paths.EXECUTIONS_KEY.format(test_execution_id_or_key), params=kwargs)

    def update_test_execution(self, test_execution_id_or_key: Union[str, int], **kwargs):
        """
        Update the test execution.

        :param test_execution_id_or_key: The ID or key of the test execution.
        Test execution keys are of the format [A-Z]+-E[0-9]+
        :return: dict with response body
        """
        return self.session.put(Paths.EXECUTIONS_KEY.format(test_execution_id_or_key), json=kwargs)

    def get_test_steps(self, test_execution_id_or_key: Union[str, int], **kwargs):
        """
        Returns the test steps for the given test execution. Provides a paged response.

        :param test_execution_id_or_key: The ID or key of the test execution.
        Test execution keys are of the format [A-Z]+-E[0-9]+
        """
        return self.session.get_paginated(Paths.EXECUTIONS_STEPS.format(test_execution_id_or_key),
                                          params=kwargs)

    def get_links(self, test_execution_id_or_key: Union[str, int]):
        """
        Returns links for a test execution with specified ID

        :param test_execution_id_or_key: The ID or key of the test execution.
        """
        return self.session.get(Paths.EXECUTIONS_LINKS.format(test_execution_id_or_key))

    def create_issue_links(self, test_execution_id_or_key: Union[str, int], issue_id: int):
        """
        Creates a link between a test execution and a Jira issue

        :param test_execution_id_or_key: The ID or key of the test execution.
        :param issue_id: The id of the issue
        :return: dict with response body
        """
        return self.session.post(Paths.EXECUTIONS_ISSUES.format(test_execution_id_or_key),
                                 json={"issueId": issue_id})


class FolderEndpoints(EndpointTemplate):
    """Api wrapper for "Folder" endpoints"""

    def get_folders(self, **kwargs):
        """
        Returns all folder.
        """
        return self.session.get_paginated(Paths.FOLDERS, params=kwargs)

    def create_folder(self, name: str, project_key: str, folder_type: str, **kwargs):
        """
        Creates a folder.

        :param name: folder name
        :param project_key: Jira project key
        :param folder_type: Folder type. Valid values: "TEST_CASE", "TEST_PLAN", "TEST_CYCLE"
        :return: dict with response body
        """
        json = {"name": name,
                "projectKey": project_key,
                "folderType": folder_type}
        json.update(kwargs)
        return self.session.post(Paths.FOLDERS, json=json)

    def get_folder(self, folder_id: int):
        """
        Returns a folder for the given ID.

        :param folder_id: Folder ID
        :return: dict with response body
        """
        return self.session.get(Paths.FOLDER_KEY.format(folder_id))


class StatusEndpoints(EndpointTemplate):
    """Api wrapper for "Status" endpoints"""

    def get_statuses(self, **kwargs):
        """Returns all statuses"""
        return self.session.get_paginated(Paths.STATUSES, params=kwargs)

    def create_status(self, project_key: str, status_name: str, status_type: str, **kwargs):
        """
        Creates a status.

        :param project_key: Jira project key
        :param status_name: The status name
        :param status_type: The status type. Valid values: "TEST_CASE", "TEST_PLAN", "TEST_CYCLE", "TEST_EXECUTION"
        :return: dict with response body
        """
        json = {"projectKey": project_key,
                "name": status_name,
                "type": status_type}
        json.update(kwargs)
        return self.session.post(Paths.STATUSES, json=json)

    def get_status(self, status_id: int):
        """
        Returns a status for the given ID

        :param status_id: Status ID
        :return: dict with response body
        """
        return self.session.get(Paths.STATUSES_ID.format(status_id))

    def update_status(self, status_id: int, project_id: int, status_name: str,
                      index: int, archived: bool, default: bool, **kwargs):
        """
        Update an existing status. Please take into account that for each non-specified field
        the value will be cleared.

        :param status_id: Status ID
        :param project_id: Project ID
        :param status_name: The status name
        :param index: The status index
        :param archived: The status archived flag
        :param default: The status default flag
        :return: dict with response body
        """
        json = {"id": status_id,
                "project": {"id": project_id},
                "name": status_name,
                "index": index,
                "archived": archived,
                "default": default}
        json.update(kwargs)
        return self.session.put(Paths.STATUSES_ID.format(status_id), json=json)


class PriorityEndpoints(EndpointTemplate):
    """Api wrapper for "Priority" endpoints"""

    def get_priorities(self, **kwargs):
        """Returns all priorities"""
        return self.session.get_paginated(Paths.PRIORITIES, params=kwargs)

    def create_priority(self, project_key: str, priority_name: str, **kwargs):
        """
        Creates a priority.

        :param project_key: Jira project key
        :param priority_name: The priority name
        :return: dict with response body
        """
        json = {"projectKey": project_key,
                "name": priority_name}
        json.update(kwargs)
        return self.session.post(Paths.PRIORITIES, json=json)

    def get_priority(self, priority_id: int):
        """
        Returns a priority for the given ID

        :param priority_id: Priority ID
        :return: dict with response body
        """
        return self.session.get(Paths.PRIORITIES_ID.format(priority_id))

    def update_priority(self, priority_id: int, project_id: int, priority_name: str,
                        index: int, default: bool, **kwargs):
        """
        Update an existing priority. Please take into account that for each non-specified field
        the value will be cleared.

        :param priority_id: Priority ID
        :param project_id: Project ID
        :param priority_name: The priority name
        :param index: The priority index
        :param default: The priority default flag
        :return: dict with response body
        """
        json = {"id": priority_id,
                "project": {"id": project_id},
                "name": priority_name,
                "index": index,
                "default": default}
        json.update(kwargs)
        return self.session.put(Paths.PRIORITIES_ID.format(priority_id), json=json)


class EnvironmentEndpoints(EndpointTemplate):
    """Api wrapper for "Environment" endpoints"""

    def get_environments(self, **kwargs):
        """Returns all environments"""
        return self.session.get_paginated(Paths.ENVIRONMENTS, params=kwargs)

    def get_environment(self, environment_id: int):
        """
        Returns an environment for the given ID

        :param environment_id: Environment ID
        :return: dict with response body
        """
        return self.session.get(Paths.ENVIRONMENTS_ID.format(environment_id))


class ProjectEndpoints(EndpointTemplate):
    """Api wrapper for "Project" endpoints"""

    def get_projects(self):
        """Returns all projects"""
        return self.session.get_paginated(Paths.PROJECTS)

    def get_project(self, project_id_or_key: Union[str, int]):
        """
        Returns a project for the given ID or key

        :param project_id_or_key: The ID or key of the Jira project
        """
        return self.session.get(Paths.PROJECTS_KEY.format(project_id_or_key))


class LinkEndpoints(EndpointTemplate):
    """Api wrapper for "Link" endpoints"""

    def delete_link(self, link_id: int):
        """Deletes a link for the given ID.

        :param link_id: The id of a link to delete
        :return: dict with response body
        """
        return self.session.delete(Paths.LINKS_ID.format(link_id))


class IssueLinksEndpoints(EndpointTemplate):
    """
    Api wrapper for "Issue Links" endpoints

    Operations related to coverage of issue links.
    """

    def get_test_cases(self, issue_key: str):
        """
        Get test case keys and versions linked to the given Jira issue.

        :param issue_key: The key of the Jira issue
        :return: dict with response body
        """
        return self.session.get(Paths.ISLINKS_CASES.format(issue_key))

    def get_test_cycles(self, issue_key: str):
        """
        Get test cycle IDs linked to the given Jira issue.

        :param issue_key: The key of the Jira issue
        :return: dict with response body
        """
        return self.session.get(Paths.ISLINKS_CYCLES.format(issue_key))

    def get_test_plans(self, issue_key: str):
        """
        Get test plan IDs linked to the given Jira issue.

        :param issue_key: The key of the Jira issue
        :return: dict with response body
        """
        return self.session.get(Paths.ISLINKS_PLANS.format(issue_key))

    def get_test_executions(self, issue_key: str):
        """
        Get test execution IDs linked to the given Jira issue.

        :param issue_key: The key of the Jira issue
        :return: dict with response body
        """
        return self.session.get(Paths.ISLINKS_EXECS.format(issue_key))


class AutomationEndpoints(EndpointTemplate):
    """
    Api wrapper for "Automation" endpoints.

    Operations related to test case automations.
    """

    def _post_reports(self,
                      path,
                      project_key,
                      file_path,
                      auto_create=False,
                      test_cycle=None,
                      **kwargs):
        """
        Post various reports logic.

        :param path: str with resource path
        :param project_key: str with project key
        :param file_path: str with path to .zip archive with report files
        :param auto_create: indicate if test cases should be created if non existent
        :param test_cycle: dict with test cycle description data
        """
        params = {'projectKey': project_key}
        to_files = None

        if auto_create:
            params.update({'autoCreateTestCases': True})

        if test_cycle:
            to_files = {'testCycle': (None, dumps(test_cycle), 'application/json')}

        return self.session.post_file(path,
                                      file_path,
                                      to_files=to_files,
                                      params=params,
                                      **kwargs)

    def post_custom_format(self,
                           project_key,
                           file_path,
                           auto_create=False,
                           test_cycle=None,
                           **kwargs):
        """
        Create results using Zephyr Scale's custom results format.

        :param project_key: str with project key
        :param file_path: str with path to .zip archive with report files
        :param auto_create: indicate if test cases should be created if non existent
        :param test_cycle: dict with test cycle description data
        """
        return self._post_reports(Paths.AUT_CUSTOM,
                                  project_key=project_key,
                                  file_path=file_path,
                                  auto_create=auto_create,
                                  test_cycle=test_cycle,
                                  **kwargs)

    def post_cucumber_format(self,
                             project_key,
                             file_path,
                             auto_create=False,
                             test_cycle=None,
                             **kwargs):
        """
        Create results using the Cucumber results format.

        :param project_key: str with project key
        :param file_path: str with path to .zip archive with report files
        :param auto_create: indicate if test cases should be created if non existent
        :param test_cycle: dict with test cycle description data
        """
        return self._post_reports(Paths.AUT_CUCUMBER,
                                  project_key=project_key,
                                  file_path=file_path,
                                  auto_create=auto_create,
                                  test_cycle=test_cycle,
                                  **kwargs)

    def post_junit_xml_format(self,
                              project_key,
                              file_path,
                              auto_create=False,
                              test_cycle=None,
                              **kwargs):
        """
        Create results using the JUnit XML results format.

        :param project_key: str with project key
        :param file_path: str with path to .zip archive with report files
        :param auto_create: indicate if test cases should be created if non existent
        :param test_cycle: dict with test cycle description data
        """
        return self._post_reports(Paths.AUT_JUNIT,
                                  project_key=project_key,
                                  file_path=file_path,
                                  auto_create=auto_create,
                                  test_cycle=test_cycle,
                                  **kwargs)

    def get_testcases_zip(self, project_key: str):
        """
        Retrieve a zip file containing Cucumber Feature Files that matches
        the query passed as parameter.

        :param project_key: Jira project key filter
        """
        params = {"projectKey": project_key}
        headers = {"Accept": "application/zip"}
        return self.session.get(Paths.AUT_CASES,
                                return_raw=True,
                                params=params,
                                headers=headers)


class HealthcheckEndpoints(EndpointTemplate):
    """Api wrapper for "Healthcheck" endpoints"""

    def get_health(self):
        """Check the health of this API."""
        return self.session.get(Paths.HEALTHCHECK)
