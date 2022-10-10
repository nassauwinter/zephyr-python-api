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
        return self.session.get(Paths.PLAN_SEARCH, params=params)
