"""Paths to form Server API URLs"""


class ServerPaths:
    """
    Zephyr Squad Server API (v1) paths based on:
    https://zephyrsquadserver.docs.apiary.io/
    https://support.smartbear.com/zephyr-squad-server/docs/api/index.html
    """

    _JIRA_API = "rest/api/latest"
    _ZEPHYR_API = "rest/zapi/latest"

    # ZQL
    ZQL_SEARCH = _ZEPHYR_API + "/zql/executeSearch"
    ZQL_CLAUSES = _ZEPHYR_API + "/zql/clauses"
    ZQL_AUTOCOMP = _ZEPHYR_API + "/zql/autocompleteZQLJson"
    ZQL_FILTER = _ZEPHYR_API + "/zql/executionFilter"
    ZQL_FILTER_ID = _ZEPHYR_API + "/zql/executionFilter/{}"
    ZQL_FILTER_COPY = _ZEPHYR_API + "/zql/executionFilter/copy"
    ZQL_FILTER_FAV = _ZEPHYR_API + "/zql/executionFilter/toggleFav"
    ZQL_FILTER_USER = _ZEPHYR_API + "/zql/executionFilter/user"
    ZQL_FILTER_RENAME = _ZEPHYR_API + "/zql/executionFilter/rename"
    ZQL_FILTER_QUICK_SEARCH = _ZEPHYR_API + "/zql/executionFilter/quickSearch"

    # Test Case
    CASE = _JIRA_API + "/issue"
    CASE_KEY = _JIRA_API + "/issue/{}"
    ISSUE_DEFAULT = _ZEPHYR_API + "/issues/default"

    # Test
    TESTS_COUNT = _ZEPHYR_API + "/test/count"
    TESTS_LABEL = _ZEPHYR_API + "/test/summary/testsbylabel"

    # Test Cycle
    CYCLE = _ZEPHYR_API + "/cycle"
    CYCLE_ID = _ZEPHYR_API + "/cycle/{}"
    CYCLE_FOLDERS = _ZEPHYR_API + "/cycle/{}/folders"
    CYCLE_BY_VER_SPR = _ZEPHYR_API + "/cycle/cyclesByVersionsAndSprint"

    # Test Execution
    EXEC = _ZEPHYR_API + "/execution"
    EXEC_ID = _ZEPHYR_API + "/execution/{}"
    EXEC_EXECUTE = _ZEPHYR_API + "/execution/{}/execute"
    EXEC_DEF = _ZEPHYR_API + "/execution/{}/defects"
    EXEC_DEL = _ZEPHYR_API + "/execution/deleteExecutions"
    EXEC_BY_ISSUE = _ZEPHYR_API + "/execution/executionsByIssue"
    EXEC_COUNT_BY_CYCLE = _ZEPHYR_API + "/execution/executionsStatusCountByCycle"
    CASE_TO_CYCLE = _ZEPHYR_API + "/execution/addTestsToCycle"
    EXEC_JOB_PROG = _ZEPHYR_API + "/execution/jobProgress/{}"

    # Test Step
    STEP_ISSUE = _ZEPHYR_API + "/teststep/{}"
    STEP_ISSUE_ID = _ZEPHYR_API + "/teststep/{}/{}"
    STEP_ISSUE_MOVE = _ZEPHYR_API + "/teststep/{}/{}/move"
    STEP_ISSUE_CLONE = _ZEPHYR_API + "/teststep/{}/clone/{}"
    STEP_ISSUE_COPY = _ZEPHYR_API + "/teststep/{}/copyteststeps"

    # Test Step Result
    STEP_RES = _ZEPHYR_API + "/stepResult"
    STEP_RES_ID = _ZEPHYR_API + "/stepResult/{}"
    STEP_RES_DEF = _ZEPHYR_API + "/stepResult/{}/defects"
    STEP_RES_EXEC_DEF = _ZEPHYR_API + "/stepResult/stepDefects"

    # Traceability
    EXEC_BY_TEST = _ZEPHYR_API + "/traceability/executionsByTest"

    # Folder
    FOLDER_ID = _ZEPHYR_API + "/folder/{}"
    FOLDER_CREATE = _ZEPHYR_API + "/folder/create"

    # Attachment
    ATTACH = _ZEPHYR_API + "/attachment"
    ATTACH_ID = _ZEPHYR_API + "/attachment/{}"
    ATTACH_ENT = _ZEPHYR_API + "/attachment/attachmentsByEntity"
    ATTACH_FILE = _ZEPHYR_API + "/attachment/{}/file"

    # Project
    PRJ_ID = _JIRA_API + "/project/{}"
    PRJ_VERSIONS_BY_KEY = _JIRA_API + "/project/{}/versions"

    # Util
    UTIL_VER_LIST = _ZEPHYR_API + "/util/versionBoard-list"
    UTIL_PROJ_LIST = _ZEPHYR_API + "/util/project-list"
    UTIL_VER_TEXT = _ZEPHYR_API + "/util/allversionstext"
    CASE_ISSUE_TYPE = _ZEPHYR_API + "/util/zephyrTestIssueType"
    SPRINT_PROJ_VER = _ZEPHYR_API + "/util/sprintsByProjectAndVersion"
    UTIL_CRITERIA = _ZEPHYR_API + "/util/cycleCriteriaInfo"

    # Preference
    STEP_PREF = _ZEPHYR_API + "/preference/getteststepcustomization"
    CYCLE_PREF = _ZEPHYR_API + "/preference/getcyclesummarycustomization"
    EXEC_PREF = _ZEPHYR_API + "/preference/getexecutioncustomization"

    # Audit
    AUDIT = _ZEPHYR_API + "/audit"

    # License
    LICENSE = _ZEPHYR_API + "/license"

    # System Info
    SYS_INFO = _ZEPHYR_API + "/systemInfo"

    # Module Info
    MOD_INFO = _ZEPHYR_API + "/moduleInfo"

    # ZChart
    ZCHART_STATUS = _ZEPHYR_API + "/zchart/issueStatuses"
    ZCHART_TESTS = _ZEPHYR_API + "/zchart/testsCreated"
