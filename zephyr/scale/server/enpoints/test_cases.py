from ...zephyr_session import ZephyrSession


class TestCaseEndpoints:
    """Api wrapper for "Test Case" endpoints"""
    def __init__(self, session: ZephyrSession):
        self.session = session

    def create_test_case(self, project_key, name, **kwargs):
        json = {"projectKey": project_key,
                "name": name}
        json.update(kwargs)
        return self.session.post("testcase", json=json)

    def get_test_case(self, test_case_key, **params):
        return self.session.get(f"testcase/{test_case_key}", params=params)

    def update_test_case(self, test_case_key, **json):
        return self.session.put(f"testcase/{test_case_key}", json=json)

    def delete_test_case(self, test_case_key):
        return self.session.delete(f"testcase/{test_case_key}")

    def get_attachments(self, test_case_key):
        return self.session.get(f"testcase/{test_case_key}/attachments")

    def create_attachment(self, test_case_key, file_path):
        with open(file_path, "rb") as file:
            files = {"file": file}
            return self.session.post(f"testcase/{test_case_key}/attachments", files=files)

    def get_latest_result(self, test_case_key):
        return self.session.get(f"testcase/{test_case_key}/testresult/latest")

    def get_step_attachments(self, test_case_key, step_index):
        return self.session.get(f"testcase/{test_case_key}/step/{step_index}/attachments")

    def create_step_attachment(self, test_case_key, step_index, file_path):
        with open(file_path, "rb") as file:
            files = {"file": file}
            return self.session.post(f"testcase/{test_case_key}/step/{step_index}/attachments", files=files)

    def search_cases(self, query, **params):
        params.update({"query": query})
        return self.session.get("testcase/search", params=params)
