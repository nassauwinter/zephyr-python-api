from json import dumps

from zephyr.scale.zephyr_scale_session import ZephyrScaleSession


class AutomationEndpoints:
    """Api wrapper for "Automation" endpoints"""

    def __init__(self, session: ZephyrScaleSession):
        self.session = session

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
        return self._post_reports('automations/executions/custom',
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
        return self._post_reports('automations/executions/cucumber',
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
        return self._post_reports('automations/executions/junit',
                                  project_key=project_key,
                                  file_path=file_path,
                                  auto_create=auto_create,
                                  test_cycle=test_cycle,
                                  **kwargs)

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
