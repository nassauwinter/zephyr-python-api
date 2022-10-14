from ...zephyr_session import ZephyrSession
from .paths import ServerPaths as Paths


class EndpointTemplate:
    def __init__(self, session: ZephyrSession):
        self.session = session


class TestCaseEndpoints(EndpointTemplate):
    """Api wrapper for "Test Case" endpoints"""

    def create_test_case(self, project_key, name, **kwargs):
        json = {"projectKey": project_key,
                "name": name}
        json.update(kwargs)
        return self.session.post(Paths.CASE, json=json)

    def get_test_case(self, test_case_key, **params):
        return self.session.get(Paths.CASE_KEY.format(test_case_key),
                                params=params)

    def update_test_case(self, test_case_key, **json):
        return self.session.put(Paths.CASE_KEY.format(test_case_key),
                                json=json)

    def delete_test_case(self, test_case_key):
        return self.session.delete(Paths.CASE_KEY.format(test_case_key))

    def get_attachments(self, test_case_key):
        return self.session.get(Paths.CASE_ATTACH.format(test_case_key))

    def create_attachment(self, test_case_key, file_path):
        return self.session.post_file(Paths.CASE_ATTACH.format(test_case_key),
                                      file_path)

    def get_latest_result(self, test_case_key):
        return self.session.get(Paths.CASE_LATEST_RES.format(test_case_key))

    def get_step_attachments(self, test_case_key, step_index):
        return self.session.get(Paths.CASE_STP_ATTACH.format(test_case_key, step_index))

    def create_step_attachment(self, test_case_key, step_index, file_path):
        return self.session.post(Paths.CASE_STP_ATTACH.format(test_case_key, step_index),
                                 file_path)

    def search_cases(self, query, **params):
        params.update({"query": query})
        return self.session.get(Paths.CASE_SEARCH, params=params)

    def get_all_versions(self, test_case_key, **params):
        """Get all test case versions ids by its key name. Undocumented in API"""
        return self.session.get(Paths.CASE_VERS.format(test_case_key), params=params)


class TestPlanEndpoints(EndpointTemplate):
    """Api wrapper for "Test Plan" endpoints"""

    def create_test_plan(self, project_key, name, **kwargs):
        json = {"projectKey": project_key,
                "name": name}
        json.update(kwargs)
        return self.session.post(Paths.PLAN, json=json)

    def get_test_plan(self, test_plan_key, **params):
        return self.session.get(Paths.PLAN_KEY.format(test_plan_key),
                                params=params)

    def update_test_plan(self, test_plan_key, **json):
        return self.session.put(Paths.PLAN_KEY.format(test_plan_key),
                                json=json)

    def delete_test_plan(self, test_plan_key):
        return self.session.delete(Paths.PLAN_KEY.format(test_plan_key))

    def get_attachments(self, test_plan_key):
        return self.session.get(Paths.PLAN_ATTACH.format(test_plan_key))

    def create_attachments(self, test_plan_key, file_path):
        return self.session.post_file(Paths.PLAN_ATTACH.format(test_plan_key),
                                      file_path)

    def search_plans(self, query, **params):
        params.update({"query": query})
        return self.session.get(Paths.PLAN_SEARCH, params=params)


class TestRunEndpoints(EndpointTemplate):
    """Api wrapper for "Test Run" endpoints"""

    def create_test_run(self, project_key, name, **kwargs):
        json = {"projectKey": project_key,
                "name": name}
        json.update(kwargs)
        return self.session.post(Paths.RUN, json=json)

    def get_test_run(self, test_run_key, **params):
        return self.session.get(Paths.RUN_KEY.format(test_run_key),
                                params=params)

    def delete_test_run(self, test_run_key):
        return self.session.delete(Paths.RUN_KEY.format(test_run_key))

    def get_attachments(self, test_run_key):
        return self.session.get(Paths.RUN_ATTACH.format(test_run_key))

    def create_attachments(self, test_run_key, file_path):
        return self.session.post_file(Paths.RUN_ATTACH.format(test_run_key),
                                      file_path)

    def create_test_result(self, test_run_key, test_case_key, **json):
        return self.session.post(Paths.RUN_TEST_RESULT.format(test_run_key, test_case_key),
                                 json=json)

    def update_test_result(self, test_run_key, test_case_key, **json):
        return self.session.post(Paths.RUN_TEST_RESULT.format(test_run_key, test_case_key),
                                 json=json)

    def get_test_results(self, test_run_key):
        return self.session.get(Paths.RUN_TEST_RESULTS.format(test_run_key))

    def create_test_results(self, test_run_key, results):
        return self.session.post(Paths.RUN_TEST_RESULTS.format(test_run_key),
                                 json=results)

    def search_runs(self, query, **params):
        params.update({"query": query})
        return self.session.get(Paths.RUN_SEARCH, params=params)


class TestResultEndpoints(EndpointTemplate):
    """Api wrapper for "Test Result" endpoints"""

    def create_test_result(self, project_key, test_case_key, **json):
        data = {"projectKey": project_key,
                "testCaseKey": test_case_key}
        data.update(json)
        return self.session.post(Paths.RES, json=data)

    def get_attachments(self, test_result_id):
        return self.session.get(Paths.RES_ATTACH.format(test_result_id))

    def create_attachment(self, test_result_id, file_path):
        return self.session.post_file(Paths.RES_ATTACH.format(test_result_id), file_path)

    def get_step_attachments(self, test_result_id, step_id):
        return self.session.get(Paths.RES_STP_ATTACH.format(test_result_id, step_id))

    def create_step_attachment(self, test_result_id, step_id, file_path):
        return self.session.post_file(Paths.RES_STP_ATTACH.format(test_result_id, step_id),
                                      file_path)


class IssueLinkEndpoints(EndpointTemplate):
    """Api wrapper for "Issue Link" endpoints"""

    def get_issue_links(self, issue_key, **params):
        return self.session.get(Paths.ISSUE_CASES.format(issue_key), params=params)


class FolderEndpoints(EndpointTemplate):
    """Api wrapper for "Folder" endpoints"""

    def create_folder(self, project_key, name, folder_type):
        json = {"projectKey": project_key,
                "name": name,
                "type": folder_type}
        return self.session.post(Paths.FOLDER, json=json)

    def update_folder(self, folder_id, **json):
        return self.session.put(Paths.FOLDER_ID.format(folder_id), json=json)


class AttachmentEndpoints(EndpointTemplate):
    """Api wrapper for "Attachment" endpoints"""

    def delete_attachment(self, attachment_id):
        return self.session.delete(Paths.ATTACH.format(attachment_id))


class EnvironmentEndpoints(EndpointTemplate):
    """Api wrapper for "Environment" endpoints"""

    def get_environments(self, project_key):
        params = {"projectKey": project_key}
        return self.session.get(Paths.ENV, params=params)

    def create_environment(self, project_key, name, description=None):
        json = {"projectKey": project_key,
                "name": name,
                "description": description}
        return self.session.post(Paths.ENV, json=json)


class AutomationEndpoints(EndpointTemplate):
    """Api wrapper for "Automation" endpoints"""

    def create_cycle(self, project_key, file_path, cycle_data=None):
        return self.session.post_file(Paths.ATM_PRJ_KEY.format(project_key),
                                      file_path=file_path,
                                      data=cycle_data)

    def create_cycle_cucumber(self, project_key, file_path, cycle_data=None):
        return self.session.post_file(Paths.ATM_PRJ_KEY.format(project_key),
                                      file_path=file_path,
                                      data=cycle_data)

    def get_testcases_cucumber(self, query):
        # Get file???
        return self.session.get(Paths.ATM_CUCUMBER, params={"query": query})


class ProjectEndpoints(EndpointTemplate):
    """Api wrapper for "Project" endpoints"""

    def create_zephyr_project(self, project_key, enabled):
        json = {"projectKey": project_key,
                "enabled": enabled}
        return self.session.post(Paths.PRJ, json=json)


class CustomFieldEndpoints(EndpointTemplate):
    """Api wrapper for "Custom Field" endpoints"""

    def create_custom_field(self, project_key, name, field_type, category, **kwargs):
        json = {"projectKey": project_key,
                "name": name,
                "type": field_type,
                "category": category}
        json.update(kwargs)
        return self.session.post(Paths.CFIELD, json=json)

    def create_custom_field_opt(self, custom_field_id, option_name):
        return self.session.post(Paths.CFIELD_OPT.format(custom_field_id),
                                 json={"name": option_name})


class DeleteExecutionEndpoints(EndpointTemplate):
    """Api wrapper for "Delete Execution" endpoints"""

    def delete_execution(self, date):
        json = {"deleteExecutionsCreatedBefore": date}
        return self.session.post(Paths.DEL_EXEC, json=json)

    def get_status(self):
        return self.session.get(Paths.DEL_EXEC_STATUS)
