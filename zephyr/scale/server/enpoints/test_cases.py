from ...zephyr_session import ZephyrSession


class TestCaseEndpoints:
    """Api wrapper for "Test Case" endpoints"""
    def __init__(self, session: ZephyrSession):
        self.session = session

    def create_test_case(self, project_key, name, **kwargs):
        pass

    def get_test_case(self, test_case_key, **kwargs):
        return self.session.get(f"testcase/{test_case_key}", params=kwargs)

    def get_all_versions(self, fields="id,majorVersion"):
        return self.session.get(f"TRT-T26244/allVersions", fields=fields)

    def update_test_case(self, test_case_key, **kwargs):
        pass

    def get_attachments(self, test_case_key):
        pass

    def create_attachment(self, test_case_key, file):
        # multipart/form-data content type
        pass

    def get_latest_result(self, test_case_key):
        pass

    def get_step_attachments(self, step_index, test_case_key):
        pass

    def create_step_attachment(self, step_index, test_case_key, file):
        # multipart/form-data content type
        pass

    def search_cases(self, **kwargs):
        pass
