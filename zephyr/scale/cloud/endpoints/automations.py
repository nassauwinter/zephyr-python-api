from ...zephyr_session import ZephyrSession


class AutomationEndpoints:
    """Api wrapper for "Automation" endpoints"""

    def __init__(self, session: ZephyrSession):
        self.session = session

    def post_custom_format(self):
        """
        Create results using Zephyr Scale's custom results format.
        """
        raise NotImplemented

    def post_cucumber_format(self):
        """
        Create results using the Cucumber results format.
        """
        raise NotImplemented

    def post_junit_xml_format(self):
        """
        Create results using the JUnit XML results format. Optionally, you can send a 'testCycle' part
        in your form data to customize the created test cycle.
        """
        raise NotImplemented

    def get_testcases_zip(self, project_key):
        """
        Retrieve a zip file containing Cucumber Feature Files that matches the query passed as parameter.
        """
        params = {"projectKey": project_key}
        headers = {"Accept": "application/zip"}
        return self.session.get("automations/testcases", return_raw=True, params=params, headers=headers)
