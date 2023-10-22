from ...zephyr_session import EndpointTemplate
from .paths import ServerPaths as Paths


class TestCaseEndpoints(EndpointTemplate):
    """Api wrapper for "Test Case" endpoints"""

    def create_test_case(self, project_key, name, **kwargs):
        """Creates a new Test Case"""
        json = {"projectKey": project_key,
                "name": name}
        json.update(kwargs)
        return self.session.post(Paths.CASE, json=json)

    def get_test_case(self, test_case_key, **params):
        """Retrieve the Test Case matching the given key"""
        return self.session.get(Paths.CASE_KEY.format(test_case_key),
                                params=params)

    def update_test_case(self, test_case_key, **json):
        """Updates a Test Case"""
        return self.session.put(Paths.CASE_KEY.format(test_case_key),
                                json=json)

    def delete_test_case(self, test_case_key):
        """Delete the Test Case matching the given key"""
        return self.session.delete(Paths.CASE_KEY.format(test_case_key))

    def get_attachments(self, test_case_key):
        """Retrieve the Test Case Attachments matching the given key"""
        return self.session.get(Paths.CASE_ATTACH.format(test_case_key))

    def create_attachment(self, test_case_key, file_path):
        """Create a new attachment on the specified Test Case"""
        return self.session.post_file(Paths.CASE_ATTACH.format(test_case_key),
                                      file_path)

    def get_latest_result(self, test_case_key):
        """Retrieve the last test result for a given key"""
        return self.session.get(Paths.CASE_LATEST_RES.format(test_case_key))

    def get_step_attachments(self, test_case_key, step_index):
        """Retrieve the attachments for a test case step"""
        return self.session.get(Paths.CASE_STP_ATTACH.format(test_case_key, step_index))

    def create_step_attachment(self, test_case_key, step_index, file_path):
        """Create a new attachment on the specified Step of a Test Case"""
        return self.session.post(Paths.CASE_STP_ATTACH.format(test_case_key, step_index),
                                 file_path)

    def search_cases(self, query, **params):
        """Retrieve the Test Cases that matches the query passed as parameter"""
        params.update({"query": query})
        return self.session.get(Paths.CASE_SEARCH, params=params)

    def get_all_versions(self, test_case_key, **params):
        """Get all test case versions ids by its key name. Undocumented in API"""
        return self.session.get(Paths.CASE_VERS.format(test_case_key), params=params)


class TestPlanEndpoints(EndpointTemplate):
    """Api wrapper for "Test Plan" endpoints"""

    def create_test_plan(self, project_key, name, **kwargs):
        """Creates a new Test Plan"""
        json = {"projectKey": project_key,
                "name": name}
        json.update(kwargs)
        return self.session.post(Paths.PLAN, json=json)

    def get_test_plan(self, test_plan_key, **params):
        """Retrieve the Test Plan matching the given key"""
        return self.session.get(Paths.PLAN_KEY.format(test_plan_key),
                                params=params)

    def update_test_plan(self, test_plan_key, **json):
        """Updates a Test Plan"""
        return self.session.put(Paths.PLAN_KEY.format(test_plan_key),
                                json=json)

    def delete_test_plan(self, test_plan_key):
        """Delete the Test Plan matching the given key"""
        return self.session.delete(Paths.PLAN_KEY.format(test_plan_key))

    def get_attachments(self, test_plan_key):
        """Retrieve the Test Plan Attachments matching the given key"""
        return self.session.get(Paths.PLAN_ATTACH.format(test_plan_key))

    def create_attachments(self, test_plan_key, file_path):
        """Create a new attachment on the specified Test Plan"""
        return self.session.post_file(Paths.PLAN_ATTACH.format(test_plan_key),
                                      file_path)

    def search_plans(self, query, **params):
        """Retrieve the Test Plans that matches the query passed as parameter"""
        params.update({"query": query})
        return self.session.get(Paths.PLAN_SEARCH, params=params)


class TestRunEndpoints(EndpointTemplate):
    """Api wrapper for "Test Run" endpoints"""

    def create_test_run(self, project_key, name, **kwargs):
        """Creates a new Test Run"""
        json = {"projectKey": project_key,
                "name": name}
        json.update(kwargs)
        return self.session.post(Paths.RUN, json=json)

    def get_test_run(self, test_run_key, **params):
        """Retrieve the Test Run matching the given key"""
        return self.session.get(Paths.RUN_KEY.format(test_run_key),
                                params=params)

    def delete_test_run(self, test_run_key):
        """Delete the Test Run matching the given key"""
        return self.session.delete(Paths.RUN_KEY.format(test_run_key))

    def get_attachments(self, test_run_key):
        """Retrieve the Test Run Attachments matching the given key"""
        return self.session.get(Paths.RUN_ATTACH.format(test_run_key))

    def create_attachments(self, test_run_key, file_path):
        """Create a new attachment on the specified Test Run"""
        return self.session.post_file(Paths.RUN_ATTACH.format(test_run_key),
                                      file_path)

    def create_test_result(self, test_run_key, test_case_key, **json):
        """
        Creates a new Test Result on the specified Test Run, looking for an item that matches
        the testCaseKey and the query string filter parameters.
        """
        return self.session.post(Paths.RUN_TEST_RESULT.format(test_run_key, test_case_key),
                                 json=json)

    def update_test_result(self, test_run_key, test_case_key, **json):
        """
        Updates the last Test Result on the specified Test Run, looking for an item that matches
        the testCaseKey and the query string filter parameters. Only defined fields will be updated.
        """
        return self.session.post(Paths.RUN_TEST_RESULT.format(test_run_key, test_case_key),
                                 json=json)

    def get_test_results(self, test_run_key):
        """Retrieve All Test Results linked to a Test Run"""
        return self.session.get(Paths.RUN_TEST_RESULTS.format(test_run_key))

    def create_test_results(self, test_run_key, results):
        """
        Create new Test Results on the specified Test Run, looking for items that match
        the testCaseKey for each body item.
        """
        return self.session.post(Paths.RUN_TEST_RESULTS.format(test_run_key),
                                 json=results)

    def search_runs(self, query, **params):
        """Retrieve the Test Runs that matches the query passed as parameter"""
        params.update({"query": query})
        return self.session.get(Paths.RUN_SEARCH, params=params)


class TestResultEndpoints(EndpointTemplate):
    """Api wrapper for "Test Result" endpoints"""

    def create_test_result(self, project_key, test_case_key, **json):
        """Creates a new Test Result for a Test Case"""
        data = {"projectKey": project_key,
                "testCaseKey": test_case_key}
        data.update(json)
        return self.session.post(Paths.RES, json=data)

    def get_attachments(self, test_result_id):
        """Retrieve the Test Result Attachments matching the given id"""
        return self.session.get(Paths.RES_ATTACH.format(test_result_id))

    def create_attachment(self, test_result_id, file_path):
        """Create a new attachment on the specified Test Result"""
        return self.session.post_file(Paths.RES_ATTACH.format(test_result_id), file_path)

    def get_step_attachments(self, test_result_id, step_id):
        """
        Retrieve the Test Result Step Attachments matching the given testResultId and
        stepIndex
        """
        return self.session.get(Paths.RES_STP_ATTACH.format(test_result_id, step_id))

    def create_step_attachment(self, test_result_id, step_id, file_path):
        """Create a new attachment on the specified step of the Test Result"""
        return self.session.post_file(Paths.RES_STP_ATTACH.format(test_result_id, step_id),
                                      file_path)


class IssueLinkEndpoints(EndpointTemplate):
    """Api wrapper for "Issue Link" endpoints"""

    def get_issue_links(self, issue_key, **params):
        """Retrieve all Test Cases linked to an Issue"""
        return self.session.get(Paths.ISSUE_CASES.format(issue_key), params=params)


class FolderEndpoints(EndpointTemplate):
    """Api wrapper for "Folder" endpoints"""

    def create_folder(self, project_key, name, folder_type):
        """
        Creates a new folder for test cases, test plans or test runs.

        In order to create a new folder you must POST a json with 3 fields: projectKey,
        name and type. The field type can be filled with TEST_CASE, TEST_PLAN or TEST_RUN.
        """
        json = {"projectKey": project_key,
                "name": name,
                "type": folder_type}
        return self.session.post(Paths.FOLDER, json=json)

    def update_folder(self, folder_id, **json):
        """
        Updates a folder for test cases, test plans or test runs.

        You can only update the name or the custom field value of a folder, in order to do that
        you must PUT a json with 2 fields: name and customFields. The field name is a String and
        forward and backslashes are not allowed. The field customFields is an object with
        the key being the custom field name.
        """
        return self.session.put(Paths.FOLDER_ID.format(folder_id), json=json)


class AttachmentEndpoints(EndpointTemplate):
    """Api wrapper for "Attachment" endpoints"""

    def delete_attachment(self, attachment_id):
        """Delete an Attachment given an id"""
        return self.session.delete(Paths.ATTACH.format(attachment_id))


class EnvironmentEndpoints(EndpointTemplate):
    """Api wrapper for "Environment" endpoints"""

    def get_environments(self, project_key):
        """
        Retrieve the Environments matching the given projectKey.

        The project must exist.
        The project must have Zephyr Scale enabled.
        """
        params = {"projectKey": project_key}
        return self.session.get(Paths.ENV, params=params)

    def create_environment(self, project_key, name, description=None):
        """
        Creates a new Environment.

        The project must exist
        The project must have Zephyr Scale enabled
        The name must be unique
        """
        json = {"projectKey": project_key,
                "name": name,
                "description": description}
        return self.session.post(Paths.ENV, json=json)


class AutomationEndpoints(EndpointTemplate):
    """Api wrapper for "Automation" endpoints"""

    def create_cycle(self, project_key, file_path, cycle_data=None):
        """
        Creates a new Test Cycle based on provided automated test results.

        This endpoint receives a zip file containing one or more Zephyr Scale Test Results File
        Format to create the Test Cycle. See Zephyr Scale JUnit Integration
        (https://bitbucket.org/smartbeartm4j/tm4j-junit-integration) to learn how
        to generate this file. Optionally, you can send a testCycle part in your form data
        to customize the created Test Cycle.
        """
        return self.session.post_file(Paths.ATM_PRJ_KEY.format(project_key),
                                      file_path=file_path,
                                      data=cycle_data)

    def create_cycle_cucumber(self, project_key, file_path, cycle_data=None):
        """
        Creates a new Test Cycle based on provided automated test results.

        This endpoint receives a zip file containing one or more Cucumber Json Output file
        (https://relishapp.com/cucumber/cucumber/docs/formatters/json-output-formatter).
        Optionally, you can send a testCycle part in your form data to customize
        the created Test Cycle.
        """
        # return self.session.post_file(Paths.ATM_CUCUMBER.format(project_key),
        #                               file_path=file_path,
        #                               data=cycle_data)
        raise NotImplementedError

    def get_testcases_cucumber(self, query):
        """
        Retrieve a zip file containing Cucumber Feature Files
        that matches the tql passed as parameter.
        """
        # return self.session.get(Paths.ATM_CASES, params={"tql": query})
        raise NotImplementedError


class ProjectEndpoints(EndpointTemplate):
    """Api wrapper for "Project" endpoints"""

    def create_zephyr_project(self, project_key, enabled):
        """
        Create a Zephyr Scale project for an existing Jira project.

        If the Zephyr Scale project exists, enable/disable it.
        """
        json = {"projectKey": project_key,
                "enabled": enabled}
        return self.session.post(Paths.PRJ, json=json)


class CustomFieldEndpoints(EndpointTemplate):
    """Api wrapper for "Custom Field" endpoints"""

    def create_custom_field(self, project_key, name, field_type, category, **kwargs):
        """
        Creates a new custom field for test cases, test plans, test runs, test result or folder.
        The custom fied name must be unique by project and category.

        Custom fields must have one of these categories:
        TEST_PLAN, TEST_RUN, TEST_STEP, TEST_EXECUTION, TEST_CASE or FOLDER.

        Custom fields must have of these types: SINGLE_LINE_TEXT, MULTI_LINE_TEXT, NUMBER, DATE,
        SINGLE_CHOICE_SELECT_LIST, CHECKBOX, DECIMAL, MULTI_CHOICE_SELECT_LIST or USER_LIST.
        """
        json = {"projectKey": project_key,
                "name": name,
                "type": field_type,
                "category": category}
        json.update(kwargs)
        return self.session.post(Paths.CFIELD, json=json)

    def create_custom_field_opt(self, custom_field_id, option_name):
        """
        Creates a new custom field option for SINGLE_CHOICE_SELECT_LIST or
        MULTI_CHOICE_SELECT_LIST custom field.
        """
        return self.session.post(Paths.CFIELD_OPT.format(custom_field_id),
                                 json={"name": option_name})


class DeleteExecutionEndpoints(EndpointTemplate):
    """Api wrapper for "Delete Execution" endpoints"""

    def delete_execution(self, date):
        """
        Starts the deletion process of Test Executions (also known as Test Results).

        This process only removes executions older than 3 months and it will keep
        the last test executions. Only Jira Admin users can execute this process.
        """
        json = {"deleteExecutionsCreatedBefore": date}
        return self.session.post(Paths.DEL_EXEC, json=json)

    def get_status(self):
        """Gets the status of the test execution deletion process.

        The statuses can be: IN_PROGRESS, FINISHED or FAILED."""
        return self.session.get(Paths.DEL_EXEC_STATUS)
