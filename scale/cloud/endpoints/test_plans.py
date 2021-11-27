from ...zephyr_session import ZephyrSession


class TestPlanEndpoints:
    """Api wrapper for "Test Plan" endpoints"""
    def __init__(self, session: ZephyrSession):
        self.session = session

    def get_test_plans(self, **kwargs):
        """Retrieves all test plans. Query parameters can be used to filter the results.

        Keyword arguments:
        :keyword projectKey: Jira project key filter
        :keyword maxResults: A hint as to the maximum number of results to return in each call
        :keyword startAt: Zero-indexed starting position. Should be a multiple of maxResults
        :return: dict with response body
        """
        return self.session.get_paginated("testplans", params=kwargs)
