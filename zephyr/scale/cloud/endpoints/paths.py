"""Paths to form Cloud API URLs"""


class CloudPaths:
    """
    Zephyr Scale Cloud API paths based on:
    https://support.smartbear.com/zephyr-scale-cloud/api-docs/
    """
    # Test Cases
    CASES = "testcases"
    CASE_KEY = "testcases/{}"
    CASE_LINKS = "testcases/{}/links"
    CASE_ISSUES = "testcases/{}/links/issues"
    CASE_WEBLINKS = "testcases/{}/links/weblinks"
    CASE_VERS = "testcases/{}/versions"
    CASE_VER = "testcases/{}/versions/{}"
    CASE_SCRIPT = "testcases/{}/testscript"
    CASE_STEPS = "testcases/{}/teststeps"
