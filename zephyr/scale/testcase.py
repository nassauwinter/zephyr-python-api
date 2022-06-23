class TestCases:
    """
    The class represents all the test cases.
    """
    def __init__(self, api):
        self.api = api

    def get_all_cases(self):
        pass

    def create_test_case(self):
        pass

    def get_test_case(self):
        pass


class TestCase:
    """
    The class represents a single test case.

    :param api: Zephyr api instance
    """
    def __init__(self, api, test_id):
        self.api = api
        self.test_case_data = self.api.test_cases.get_test_case(test_id)

    @property
    def id(self):
        return self.test_case_data.get("id")

    @property
    def key(self):
        return self.test_case_data.get("key")

    @property
    def name(self):
        return self.test_case_data.get("name")

    @property
    def project(self):
        project = self.test_case_data.get("project")
        res = self.api.projects.get_project(project.get("id"))
        return res.get("name")

    @property
    def objective(self):
        return self.test_case_data.get("objective")

    @property
    def precondition(self):
        return self.test_case_data.get("precondition")

    @property
    def estimated_time(self):
        return self.test_case_data.get("estimatedTime")

    @property
    def status(self):
        status = self.test_case_data.get("status")
        res = self.api.statuses.get_status(status.get("id"))
        return res.get("name")
