"""Paths to form Server API URLs"""


class ServerPaths:
    """
    Zephyr Scale Server API (v1) paths based on:
    https://support.smartbear.com/zephyr-scale-server/api-docs/v1/
    """
    # Test Case
    CASE = "testcase"
    CASE_KEY = "testcase/{}"
    CASE_ATTACH = "testcase/{}/attachments"
    CASE_LATEST_RES = "testcase/{}/testresult/latest"
    CASE_STP_ATTACH = "testcase/{}/step/{}/attachments"
    CASE_SEARCH = "testcase/search"
    CASE_VERS = "testcase/{}/allVersions"

    # Test Plan
    PLAN = "testplan"
    PLAN_KEY = "testplan/{}"
    PLAN_ATTACH = "testplan/{}/attachments"
    PLAN_SEARCH = "testplan/search"

    # Test Run
    RUN = "testrun"
    RUN_KEY = "testrun/{}"
    RUN_ATTACH = "testrun/{}/attachments"
    RUN_TEST_RESULT = "testrun/{}/testcase/{}/testresult"
    RUN_TEST_RESULTS = "testrun/{}/testresults"
    RUN_SEARCH = "testrun/search"

    # Test Result
    RES = "testresult"
    RES_ATTACH = "testresult/{}/attachments"
    RES_STP_ATTACH = "testresult/{}/step/{}/attachments"

    # Issue link
    ISSUE_CASES = "issuelink/{}/testcases"

    # Folder
    FOLDER = "folder"
    FOLDER_KEY = "folder/{}"

    # Attachments
    ATTACH = "attachments/{}"

    # Environments
    ENV = "environments"

    # Automation
    ATM_PRJ_KEY = "automation/execution/{}"
    ATM_CUCUMBER = "automation/execution/cucumber/{}"
    ATM_CASES = "automation/testcases"

    # Project
    PRJ = "project"

    # Custom Field
    CFIELD = "customfield"
    CFIELD_OPT = "customfield/{}/option"

    # Delete Execution
    DEL_EXEC = "delete/executiondeletion"
    DEL_EXEC_STATUS = "delete/executiondeletion/status"
