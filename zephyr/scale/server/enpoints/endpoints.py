from ...zephyr_session import ZephyrSession
from .paths import ServerPaths as Paths


class TestCaseEndpoints:
    """Api wrapper for "Test Case" endpoints"""
    def __init__(self, session: ZephyrSession):
        self.session = session

    def create_test_case(self, project_key, name, **kwargs):
        json = {"projectKey": project_key,
                "name": name}
        json.update(kwargs)
        return self.session.post(Paths.CASE,
                                 json=json)

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
        with open(file_path, "rb") as file:
            files = {"file": file}
            return self.session.post(Paths.CASE_ATTACH.format(test_case_key),
                                     files=files)

    def get_latest_result(self, test_case_key):
        return self.session.get(Paths.CASE_LATEST_RES.format(test_case_key))

    def get_step_attachments(self, test_case_key, step_index):
        return self.session.get(Paths.CASE_STP_ATTACH.format(test_case_key, step_index))

    def create_step_attachment(self, test_case_key, step_index, file_path):
        with open(file_path, "rb") as file:
            files = {"file": file}
            return self.session.post(Paths.CASE_STP_ATTACH.format(test_case_key, step_index),
                                     files=files)

    def search_cases(self, query, **params):
        params.update({"query": query})
        return self.session.get(Paths.CASE_SEARCH, params=params)

    def get_all_versions(self, test_case_key, **params):
        """Get all test case versions ids by its key name. Undocumented in API"""
        return self.session.get(Paths.CASE_VERS.format(test_case_key), params=params)
