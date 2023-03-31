from json import dumps

from ...zephyr_session import ZephyrSession


class AutomationEndpoints:
    """Api wrapper for "Automation" endpoints"""

    def __init__(self, session: ZephyrSession):
        self.session = session

    def post_custom_format(self):
        """
        Create results using Zephyr Scale's custom results format.
        """
        raise NotImplementedError

    def post_cucumber_format(self, project_key, file_path, auto_create=False, test_cycle=None, **kwargs):
        """
        Create results using the Cucumber results format.

        :param project_key: str with project key
        :param file_path: str with path to .zip archive with report files
        :param auto_create: indicate if test cases should be created if non existent
        :param test_cycle: dict with test cycle description data
        """
        params = {'projectKey': project_key}
        if auto_create:
            params.update({'autoCreateTestCases': True})

        to_files = {'testCycle': (None, dumps(test_cycle), 'application/json')} if test_cycle else None

        return self.session.post_file('automations/executions/cucumber',
                                      file_path,
                                      to_files=to_files,
                                      params=params,
                                      **kwargs)

    def post_junit_xml_format(self):
        """
        Create results using the JUnit XML results format. Optionally,
        you can send a 'testCycle' part in your form data to customize
        the created test cycle.
        """
        raise NotImplementedError

    def get_testcases_zip(self, project_key):
        """
        Retrieve a zip file containing Cucumber Feature Files that matches
        the query passed as parameter.
        """
        params = {"projectKey": project_key}
        headers = {"Accept": "application/zip"}
        return self.session.get("automations/testcases",
                                return_raw=True,
                                params=params,
                                headers=headers)
