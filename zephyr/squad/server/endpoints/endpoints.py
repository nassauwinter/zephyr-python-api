from zephyr.squad.zephyr_squad_session import ZephyrSquadSession
from zephyr.utils.common import dict_merge
from .paths import ServerPaths as Paths


class EndpointTemplate:
    """Class with basic constructor for endpoint classes"""
    def __init__(self, session: ZephyrSquadSession):
        self.session = session


class ChartResourceEndpoints(EndpointTemplate):
    """Api wrapper for ChartResource"""

    def get_issue_status_by_project(self, project_id):
        """Get Issue Statuses by Project Id"""
        params = {
            "projectId": project_id
        }
        return self.session.get(Paths.ZCHART_STATUS, params=params)

    def generate_test_created_data(self, project_key, **params):
        """Generate Test's Created Data by Project Key"""
        params.update(projectKey=project_key)
        return self.session.get(Paths.ZCHART_TESTS, params=params)


class ExecutionSearchResourceEndpoints(EndpointTemplate):
    """Api wrapper for ExecutionSearchResource"""

    def execute_search_to_get_search_result(self, query, **params):
        """Execute Search to Get ZQL Search Result by zqlQuery"""
        params.update(zqlQuery=f'({query})')
        return self.session.get_paginated(Paths.ZQL_SEARCH, query_type="execution", params=params)

    def get_search_clauses(self):
        """Get List of Search Clauses"""
        return self.session.get(Paths.ZQL_CLAUSES)

    def get_autocomplete_zql_json(self):
        """Get AutoComplete JSON Execution"""
        return self.session.get(Paths.ZQL_AUTOCOMP)


class ZQLFilterResourceEndpoints(EndpointTemplate):
    """
    Following section describes the rest resources (API's) pertaining to ExecutionFilterResource
    """

    def get_zql_filter(self, filter_id):
        """Get ZQL filter by it's id"""
        return self.session.get(Paths.ZQL_FILTER_ID.format(filter_id))

    def delete_zql_filter(self, filter_id):
        """Deletes a ZQL filter by id"""
        return self.session.delete(Paths.ZQL_FILTER_ID.format(filter_id))

    def get_all_execution_filters(self, **params):
        """Get All Execution Filters"""
        raise NotImplementedError

    def search_execution_filters(self, **params):
        """Search Execution Filters by Filter Name"""
        raise NotImplementedError

    def quick_search_zql_filters(self, query):
        """Quick Search Execution Filters by Query"""
        params = {
            'query': query
        }
        return self.session.get(Paths.ZQL_FILTER_QUICK_SEARCH, params=params)

    def copy_zql_filter(self, filter_id, filter_name):
        """Copy Execution Filter by Filter Name"""
        json = {
            "id": filter_id,
            "filterName": filter_name
        }
        return self.session.put(Paths.ZQL_FILTER_COPY, json=json)

    def create_execution_filter(self, **params):
        """Create new execution filter"""
        raise NotImplementedError

    def update_the_zql_filter(self, **params):
        """Update Execution Filter"""
        raise NotImplementedError

    def rename_zql_filter(self, filter_id, filter_name):
        """Rename an Execution Filter"""
        json = {
            "id": filter_id,
            "filterName": filter_name
        }
        return self.session.put(Paths.ZQL_FILTER_RENAME, json=json)

    def toggle_zql_filter_isfavorites(self, filter_id, is_favorite=True):
        """Toggle ZQL filter 'isFavorites'"""
        json = {
            "id": filter_id,
            "isFavorite": is_favorite
        }
        return self.session.put(Paths.ZQL_FILTER_FAV, json=json)

    def get_loggedin_user(self):
        """Get LoggedIn User"""
        return self.session.get(Paths.ZQL_FILTER_USER)


class CycleResourceEndpoints(EndpointTemplate):
    """Following section describes rest resources (API's) pertaining to CycleResource"""

    def get_cycle_information(self, cycle_id):
        """Get Cycle data by Cycle Id. If cycleId -1 is passed, system returns hardcoded cycle"""
        return self.session.get(Paths.CYCLE_ID.format(cycle_id))

    def export_cycle_data(self, **params):
        """Export Cycle by Cycle Id, file is generated on fly and streamed to client"""
        raise NotImplementedError

    def create_new_cycle(self, project_id, version_id, name, data=None):
        """
        Create New Cycle by given Cycle Information

        See Zephyr Squad Cycle creation documentation to better understand what can be modified.
        https://support.smartbear.com/zephyr-squad-server/docs/api/how-to/create-cycle.html
        """
        if data is None:
            data = {}

        json = {
            'name': name,
            'projectId': project_id,
            'versionId': version_id
        }
        merged_json = dict_merge(data, json)
        return self.session.post(Paths.CYCLE, json=merged_json)

    def update_cycle_information(self, **params):
        """Update Cycle Information"""
        raise NotImplementedError

    def delete_cycle(self, cycle_id, is_folder_cycle_delete=""):
        """
        Delete Cycle by Cycle Id

        This API returns a jobProgressToken which should be used for making the call to
        /rest/zapi/latest/execution/jobProgress/:jobProgressToken?type=cycle_delete_job_progress.
        Once the request is processed, the jobProgress will populate the message field with result.
        """
        params = {
            "isFolderCycleDelete": is_folder_cycle_delete,
        }
        return self.session.delete(Paths.CYCLE_ID.format(cycle_id), params=params)

    def get_list_of_cycle(self, project_id, **params):
        """Get List of Cycle by Project Id"""
        params.update(projectId=project_id)
        return self.session.get(Paths.CYCLE, params=params)

    def move_executions_to_cycle(self, **params):
        """
        Move Executions to Cycle by Cycle Id

        This API returns a jobProgressToken which should be used for making the call to
        /rest/zapi/latest/execution/jobProgress/:jobProgressToken?type=bulk_execution_copy_move_job_progress. # pylint: disable=line-too-long
        Once the request is processed, the jobProgress will populate the message field with result.
        """
        raise NotImplementedError

    def get_cycles_by_versions_sprint(self, **params):
        """Get Cycles by Version Id, Project Id"""
        raise NotImplementedError

    def clean_up_sprint_from_cycle(self, **params):
        """Cleanup sprint data from cycle"""
        raise NotImplementedError

    def get_the_list_of_folder_for_a_cycle(self, project_id, version_id, cycle_id, **params):
        """Get the list of folder for a cycle"""
        params.update(projectId=project_id, versionId=version_id)
        return self.session.get(Paths.CYCLE_FOLDERS.format(cycle_id), params=params)

    def move_selected_executions_or_all_executions_from_cycle_to_folder(self, **params):
        """Move selected executions or all executions from cycle to folder"""
        raise NotImplementedError

    def copy_executions_to_cycle(self, **params):
        """
        Copy Executions to Cycle By Cycle Id

        This API returns a jobProgressToken which should be used for making the call to
        /rest/zapi/latest/execution/jobProgress/:jobProgressToken?type=bulk_execution_copy_move_job_progress. # pylint: disable=line-too-long
        Once the request is processed, the jobProgress will populate the message field with result.
        """
        raise NotImplementedError


class ZNavResourceEndpoints(EndpointTemplate):
    """Rest end point for Zephyr Navigation(znav)"""

    def get_available_columns(self, **params):
        """Get Available Columns by Execution Filter Id"""
        raise NotImplementedError

    def create_column_selection(self, **params):
        """Create/Save Column Selection"""
        raise NotImplementedError

    def update_column_selection(self, **params):
        """Update Column Selection by Column Layout Id"""
        raise NotImplementedError


class LicenseResourceEndpoints(EndpointTemplate):
    """
    Following section describes the rest resources (API's) pertaining to Zephyr Squad
    LicenseResource
    """

    def get_license_status_information(self):
        """Get License Status Inforation"""
        return self.session.get(Paths.LICENSE)


class PreferenceResourceEndpoints(EndpointTemplate):
    """Following section describes the rest resources pertaining to PreferenceResource"""

    def set_test_step_customization_preference(self, **params):
        """Set test step customization preference."""
        raise NotImplementedError

    def get_test_step_customization_preference(self):
        """Get test step customization preference."""
        return self.session.get(Paths.STEP_PREF)

    def set_cycle_summary_columns_customization_preference(self, **params):
        """Set cycle summary columns customization preference."""
        raise NotImplementedError

    def get_cycle_summary_customization_preference(self):
        """Get cycle summary column customization preference."""
        return self.session.get(Paths.CYCLE_PREF)

    def set_execution_summary_columns_customization_preference(self, **params):
        """Set execution summary columns customization preference."""
        raise NotImplementedError

    def get_execution_summary_customization_preference(self):
        """Get execution summary column customization preference."""
        return self.session.get(Paths.EXEC_PREF)


class StepResultResourceEndpoints(EndpointTemplate):
    """Following section describes the rest resources pertaining to StepResultResource"""

    def get_list_of_step_result(self, execution_id, expand=""):
        """Get List of Step Result by Execution Id"""
        params = {
            "executionId": execution_id,
            "expand": expand
        }
        return self.session.get(Paths.STEP_RES, params=params)

    def get_step_result_information(self, step_result_id, expand=""):
        """Get Single Step Result Information by StepResult Id"""
        params = {
            "expand": expand
        }
        return self.session.get(Paths.STEP_RES_ID.format(step_result_id), params=params)

    def create_new_step_result(self, **params):
        """Create New StepResult, StepResult gets created as soon as execution is fetched"""
        raise NotImplementedError

    def update_step_result_information(self, step_result_id, status):
        """
        Update StepResult Information by StepResult Id. Available status values:
        -1 = UNEXECUTED | 1 = PASS | 2 = FAIL | 3 = WIP | 4 = BLOCKED
        """
        json = {
            "status": status
        }
        return self.session.put(Paths.STEP_RES_ID.format(step_result_id), json=json)

    def get_list_of_step_defect(self, step_result_id):
        """Get List of StepDefect by StepResult Id"""
        return self.session.get(Paths.STEP_RES_DEF.format(step_result_id))

    def get_list_of_step_defect_by_execution(self, execution_id, expand=""):
        """Get List of StepDefect by Execution Id"""
        params = {
            "executionId": execution_id,
            "expand": expand
        }
        return self.session.get(Paths.STEP_RES_EXEC_DEF, params=params)


class TraceabilityResourceEndpoints(EndpointTemplate):
    """Rest end point for Traceability"""

    def search_defect_statistics(self, **params):
        """Search Defect Statistics by Defect Id/Key List"""
        raise NotImplementedError

    def search_execution_by_efect(self, **params):
        """Get Execution by Defect Id/Key"""
        raise NotImplementedError

    def get_list_of_search_execution_by_test(self, test_id_or_key, **params):
        """Get Search Execution List by Test Id/Key"""
        params.update(testIdOrKey=test_id_or_key)
        return self.session.get(Paths.EXEC_BY_TEST, params=params)

    def get_list_of_search_test_by_requirement(self, **params):
        """Get Search Test by Requirement Id/Key"""
        raise NotImplementedError

    def export_traceability_report(self, **params):
        """Export Traceability Report by Defect Id List"""
        raise NotImplementedError


class TestcaseResourceEndpoints(EndpointTemplate):
    """Following section describes rest resources pertaining to TestcaseResource"""

    def get_test_count_list(self, project_id, version_id, group_fld="user"):
        """
        Get Count List of Tests by Project Id, Version Id.

        group_fld ("user" | "component") defaults to "user".
        """
        params = {
            "projectId": project_id,
            "versionId": version_id,
            "groupFld": group_fld
        }
        return self.session.get(Paths.TESTS_COUNT, params=params)

    def get_list_of_saved_searches(self, **params):
        """Get List of Saved Searches by SaveSearch Id"""
        raise NotImplementedError

    def add_issue_link(self, **params):
        """Add Issue Link from Issue to Zephyr Test"""
        raise NotImplementedError

    def fetch_tests_by_label(self, project_id, label_name, **params):
        """
        Fetch Tests By Label

        The labelName acts like a regex, so the word 'ak' will bring all labels that contains
        'ak' in them like 'akonadi'. The query will also return all test cases without any label
        in an entry called 'No Label'.
        """
        params.update({"projectId": project_id, "labelName": label_name})
        return self.session.get_paginated(Paths.TESTS_LABEL, query_type="test-label", params=params)

    def fetch_tests_by_component(self, **params):
        """Fetch Tests By Component"""
        raise NotImplementedError

    def fetch_tests_by_version(self, **params):
        """Fetch Tests By Version"""
        raise NotImplementedError


class UtilResourceEndpoints(EndpointTemplate):
    """Following section describes the rest resources related to common utility API(s)"""

    def get_all_versions(self, project_id, **params):
        """Get List of Versions (Releases)"""
        params.update(projectId=project_id)
        return self.session.get(Paths.UTIL_VER_LIST, params=params)

    def get_zephyr_issue_type(self):
        """Get Zephyr Issue Type"""
        return self.session.get(Paths.CASE_ISSUE_TYPE)

    def get_all_projects(self):
        """Get List of Projects"""
        return self.session.get(Paths.UTIL_PROJ_LIST)

    def get_all_versions_text(self):
        """Get All Versions Text"""
        return self.session.get(Paths.UTIL_VER_TEXT)

    def get_list_of_sprints(self, project_id, version_id):
        """Get List of Sprints by Project Id and Version Id"""
        params = {
            "projectId": project_id,
            "versionId": version_id
        }
        return self.session.get(Paths.SPRINT_PROJ_VER, params=params)

    def get_cycle_criteria_info(self, project_id):
        """Get Cycle Criteria Information"""
        params = {
            "projectId": project_id,
        }
        return self.session.get(Paths.UTIL_CRITERIA, params=params)

    def get_execution_statuses_priorities_components_labels_using_tes(self, **params):
        """Get Execution Statuses, Priorities, Components, Labels using testExecutionStatus"""
        raise NotImplementedError

    def get_execution_statuses_priorities_components_labels_using_tses(self, **params):
        """Get Execution Statuses, Priorities, Components, Labels using teststepExecutionStatus"""
        raise NotImplementedError

    def get_dashboard_summary(self, **params):
        """Get Dashboard information by Query"""
        raise NotImplementedError

    def get_components_using_cl(self, **params):
        """Gets all component for a project using component-list"""
        raise NotImplementedError

    def get_components_using_tsl(self, **params):
        """Gets all component for a project using teststatus-list"""
        raise NotImplementedError


class FolderResourceEndpoints(EndpointTemplate):
    """Following section describes rest resources pertaining to Folder Resource"""

    def create_folder_under_cycle(self, project_id, cycle_id, version_id, data=None):
        """
        Creates a Folder under the provided cycle

        See Zephyr Squad Folder creation documentation to better understand what can be modified.
        https://support.smartbear.com/zephyr-squad-server/docs/api/how-to/create-folder-in-cycle.html
        """
        if data is None:
            data = {}

        json = {
            'cycleId': cycle_id,
            'projectId': project_id,
            'versionId': version_id
        }
        merged_json = dict_merge(data, json)
        return self.session.post(Paths.FOLDER_CREATE, json=merged_json)

    def update_folder_information(self, project_id, cycle_id, version_id, folder_id, name,
                                  data=None):
        """Updates Folder information"""
        if data is None:
            data = {}

        json = {
            'cycleId': cycle_id,
            'projectId': project_id,
            'versionId': version_id,
            "folderId": folder_id,
            "name": name,
        }
        merged_json = dict_merge(data, json)
        return self.session.put(Paths.FOLDER_ID.format(folder_id), json=merged_json)

    def delete_folder_under_cycle(self, folder_id, project_id, version_id, cycle_id):
        """Deletes a Folder"""
        params = {
            "projectId": project_id,
            "versionId": version_id,
            "cycleId": cycle_id,
        }
        return self.session.delete(Paths.FOLDER_ID.format(folder_id), params=params)


class ExecutionResourceEndpoints(EndpointTemplate):
    """Following section describes rest resources (API's) pertaining to ExecutionResource"""

    def get_execution_information(self, execution_id, **params):
        """Gets all executions available for given execution Id"""
        return self.session.get(Paths.EXEC_ID.format(execution_id),
                                params=params)

    def get_list_of_execution(self, **params):
        """Get all execution available for given issue id"""
        raise NotImplementedError

    def get_defect_list(self, execution_id):
        """Get all defect available for given Execution Id"""
        return self.session.get(Paths.EXEC_DEF.format(execution_id))

    def add_assignee_to_execution(self, execution_id, assignee):
        """Add Assignee to execution by Execution Id"""
        params = {
            'assignee': assignee
        }
        return self.session.post(Paths.EXEC_ID.format(execution_id), params=params)

    def create_new_execution(self, project_id, version_id, cycle_id, issue_id, data=None):
        """Use this resource to create new execution"""
        if data is None:
            data = {}

        json = {
            'projectId': project_id,
            'versionId': version_id,
            'cycleId': cycle_id,
            'issueId': issue_id
        }
        merged_json = dict_merge(data, json)
        return self.session.post(Paths.EXEC, json=merged_json)

    def get_execution_count_summary(self, **params):
        """
        Get Execution Count List.

        It takes care of 3 execution counts
        1. execution summary - projectId + groupFld:timePeriod
        2. test execution gadget - projectId + version + groupFld:cycle|user|component
        3. burndown - projectId + versionId + cycleId + groupFld:timePeriod
        """
        raise NotImplementedError

    def get_top_defect_by_issue_status(self, **params):
        """Get Defect List by Project Id, Version Id, Issue Status"""
        raise NotImplementedError

    def re_index_all_execution(self, **params):
        """
        Re Index all Execution

        This API returns a jobProgressToken which should be used for making the call to
        /rest/zapi/latest/execution/jobProgress/:jobProgressToken?type=reindex_job_progress.
        Once the request is processed, the jobProgress will populate the message field with result.
        """
        raise NotImplementedError

    def re_index_all_execution_for_current_node(self, **params):
        """
        Re Index all Execution for Current Node

        This API returns a jobProgressToken which should be used for making the call to
        /rest/zapi/latest/execution/jobProgress/:jobProgressToken?type=reindex_job_progress.
        Once the request is processed, the jobProgress will populate the message field with result.
        """
        raise NotImplementedError

    def re_index_all_execution_for_given_project_ids(self, **params):
        """
        Re Index all Execution for given project id(s)

        This API returns a jobProgressToken which should be used for making the call to
        /rest/zapi/latest/execution/jobProgress/:jobProgressToken?type=reindex_job_progress.
        Once the request is processed, the jobProgress will populate the message field with result.
        """
        raise NotImplementedError

    def get_index_status(self, **params):
        """Get Index Status by Token"""
        raise NotImplementedError

    def get_job_progress_status(self, job_progress_token, **params):
        """Get job progress with status"""
        return self.session.get(Paths.EXEC_JOB_PROG.format(job_progress_token), params=params)

    def update_bulk_defects(self, **params):
        """
        Update bulk Defect by Executions, Defects

        This API returns a jobProgressToken which should be used for making the call to
        /rest/zapi/latest/execution/jobProgress/:jobProgressToken?type=bulk_execution_associate_defect_job_progress. # pylint: disable=line-too-long
        Once the request is processed, the jobProgress will populate the message field with result.
        """
        raise NotImplementedError

    def update_execution_details(self, execution_id, status, data=None):
        """
        Update Execution Details by Execution Id. Available status values:
        -1 = UNEXECUTED | 1 = PASS | 2 = FAIL | 3 = WIP | 4 = BLOCKED
        """
        if data is None:
            data = {}

        json = {
            "status": status
        }
        merged_json = dict_merge(data, json)

        return self.session.put(Paths.EXEC_EXECUTE.format(execution_id), json=merged_json)

    def delete_execution(self, execution_id):
        """Execution with the given Id will be deleted."""
        return self.session.delete(Paths.EXEC_ID.format(execution_id))

    def add_test_to_cycle(self, project_id, cycle_id, method, data=None):
        """
        Add Test to Cycle

        This API will execute based on following conditions:
        1. From individual test required following params:
           (assigneeType, cycleId, issues, method = 1, projectId, versionId)
        2. From search filter required following params:
           (assigneeType, cycleId, issues, method = 2, projectId, versionId, searchId)
        3. From another cycle required following params:
           (assigneeType, cycleId, issues, method = 3, projectId, versionId, components,
            fromCycleId, fromVersionId, hasDefects, labels, priorities, statuses)

        This API returns a jobProgressToken which should be used for making the call to
        /rest/zapi/latest/execution/jobProgress/:jobProgressToken?type=add_tests_to_cycle_job_progress. # pylint: disable=line-too-long
        Once the request is processed, the jobProgress will populate the message field with result.

        See Zephyr Squad documentation to better understand what can be modified.
        https://support.smartbear.com/zephyr-squad-server/docs/api/how-to/add-tests-to-cycle.html
        """
        if data is None:
            data = {}

        json = {
            'cycleId': cycle_id,
            'projectId': project_id,
            'method': method
        }
        merged_json = dict_merge(data, json)
        return self.session.post(Paths.CASE_TO_CYCLE, json=merged_json)

    def refresh_issue_link_status(self, **params):
        """Refresh Link Status(not found/in progress/completed)"""
        raise NotImplementedError

    def export_execution(self, **params):
        """Export Selected Execution by Selected Export Format(RSS/HTML/XLS/CSV/XML)"""
        raise NotImplementedError

    def navigate_execution(self, **params):
        """
        Validates and executes search against zephyr indexes. offset and limit provides a way to
        define the beginning and the max limit allowed
        """
        raise NotImplementedError

    def re_order_execution(self, **params):
        """Re Order Execution"""
        raise NotImplementedError

    def get_execution_summaries_by_sprint_and_issue(self, **params):
        """Gets all execution available for given Issue Id"""
        raise NotImplementedError

    def get_execution_summary_by_issue(self, **params):
        """Gets all execution available for given Issue Id"""
        raise NotImplementedError

    def get_executions_count_for_cycles_by_given_project_id_and_version_id(self, **params):
        """Get Executions count for cycles by given project id and version id"""
        raise NotImplementedError

    def get_executions_count_for_given_cycle(self, **params):
        """Get Executions count for given cycle"""
        raise NotImplementedError

    def get_executions_count_per_assignee_for_given_cycle(self, **params):
        """Get Executions count per assignee for given cycle"""
        raise NotImplementedError

    def delete_bulk_execution(self, execution_id):
        """
        Delete bulk Execution by Execution Id

        This API returns a jobProgressToken which should be used for making the call to
        /rest/zapi/latest/execution/jobProgress/:jobProgressToken?type=bulk_executions_delete_job_progress. # pylint: disable=line-too-long
        Once the request is processed, the jobProgress will populate the message field with result.
        """
        if not isinstance(execution_id, list):
            execution_id = [ execution_id ]

        json = {
            "executions": execution_id
        }
        return self.session.delete(Paths.EXEC_DEL, json=json)

    def refresh_issue_remote_link(self, **params):
        """Refresh Issue to Test/Step Link or Remote Link"""
        raise NotImplementedError

    def assign_bulk_executions(self, **params):
        """
        Add bulk execution with assignee type

        This API returns a jobProgressToken which should be used for making the call to
        /rest/zapi/latest/execution/jobProgress/:jobProgressToken?type=bulk_execution_assign_user_job_progress. # pylint: disable=line-too-long
        Once the request is processed, the jobProgress will populate the message field with result.
        """
        raise NotImplementedError

    def update_bulk_execution_status(self, **params):
        """
        Update bulk Execution Status by Status

        This API returns a jobProgressToken which should be used for making the call to
        /rest/zapi/latest/execution/jobProgress/:jobProgressToken?type=update_bulk_execution_status_job_progress. # pylint: disable=line-too-long
        Once the request is processed, the jobProgress will populate the message field with result.
        """
        raise NotImplementedError


class IssuePickerResourceEndpoints(EndpointTemplate):
    """Following section describes the rest resources pertaining to IssuePickerResource"""

    def get_issues_for_test(self, **params):
        """Get Issues Data for Test by Query"""
        raise NotImplementedError

    def get_default_issue_type(self, project_id):
        """Get Default Issue Type by Project Id"""
        params = {
            "projectId": project_id
        }
        return self.session.get(Paths.ISSUE_DEFAULT, params=params)


class AuditResourceEndpoints(EndpointTemplate):
    """Following section describes the rest resources pertaining to AuditResource"""

    def get_audit_log(self, **params):
        """Get Audit Log by Entity Type, Event, User"""
        raise NotImplementedError


class TeststepResourceEndpoints(EndpointTemplate):
    """Following section describes the rest resources pertaining to TestStepResource"""

    def delete_teststep(self, issue_id, test_step_id):
        """Delete TestStep by TestStep Id, Issue Id"""
        return self.session.delete(Paths.STEP_ISSUE_ID.format(issue_id, test_step_id))

    def get_teststep_information(self, issue_id, test_step_id):
        """Get TestStep Information by TestStep Id, IssueId"""
        return self.session.get(Paths.STEP_ISSUE_ID.format(issue_id, test_step_id))

    def update_teststep_data(self, issue_id, test_step_id,
                             test_step=None, step_data=None, step_result=None):
        """Update TestStep Information by TestStep Id, Issue Id"""
        json = {}
        if test_step is not None:
            json['step'] = test_step
        if step_data is not None:
            json['data'] = step_data
        if step_result is not None:
            json['result'] = step_result
        return self.session.put(Paths.STEP_ISSUE_ID.format(issue_id, test_step_id), json=json)

    def get_list_of_teststeps(self, issue_id, **params):
        """Get List of TestSteps by Issue Id. 'offset' and 'limit' are optional"""
        return self.session.get(Paths.STEP_ISSUE.format(issue_id), params=params)

    def create_new_teststep(self, issue_id, test_step=None, step_data=None, step_result=None):
        """Create New TestStep by Issue Id"""
        json = {
            'step': test_step,
            'data': step_data,
            'result': step_result
        }
        return self.session.post(Paths.STEP_ISSUE.format(issue_id), json=json)

    def move_teststep_to_issue(self, issue_id, test_step_id, after_id=None):
        """
        Move TestStep to Issue.

        The API call considers the 'First' position to be last 'Order Id'. If no after_id element
        is given, the element is moved by default on the 'First' position.
        """
        json = {}
        if after_id:
            json['after'] = "/jira/" + Paths.STEP_ISSUE_ID.format(issue_id, after_id)
        else:
            json['position'] = "First"
        return self.session.post(Paths.STEP_ISSUE_MOVE.format(issue_id, test_step_id), json=json)

    def clone_teststep(self, issue_id, test_step_id, position=-1):
        """Clone TestStep by from TestStep Id, Issue Id"""
        json = {
            'position': position
        }
        return self.session.post(Paths.STEP_ISSUE_CLONE.format(issue_id, test_step_id), json=json)

    def copy_test_steps_from_source_to_destination_issues(self, issue_key, destination_issues,
            is_jql=False, copy_attachments=False, copy_custom_field=False):
        """
        Copy Test steps from source to destination issues. The keys should be used in all instances.

        This API returns a jobProgressToken which should be used for making the call to
        /rest/zapi/latest/execution/jobProgress/:jobProgressToken?type=copy_test_step_job_progress.
        Once the request is processed, the jobProgress will populate the message field with result.
        """
        if not isinstance(destination_issues, list):
            destination_issues = [ destination_issues ]

        json = {
            'destinationIssues': ','.join(destination_issues),
            'copyAttachments': copy_attachments,
            'copyCustomField': copy_custom_field,
            'isJql': is_jql
        }
        return self.session.post(Paths.STEP_ISSUE_COPY.format(issue_key), json=json)


class AttachmentResourceEndpoints(EndpointTemplate):
    """
    Following section describes the rest resources (API's) for fetching and uploading attachments.
    To get attachment for a given entity (Execution or Its Stepresults) or upload, You would need
    its id: Unique Identifier in DB Type: execution | stepresult
    """

    def delete_attachment(self, attach_file_id):
        """Delete Attachment by Attachment Id"""
        return self.session.delete(Paths.ATTACH_ID.format(attach_file_id))

    def get_single_attachment(self, attach_file_id):
        """Get Attachment Details by Attachment Id"""
        return self.session.get(Paths.ATTACH_ID.format(attach_file_id))

    def add_attachment_into_entity(self, file_path, entity_id, entity_type):
        """Add Attachment into Entity by Entity Id, Entity Type"""
        params = {
            'entityId': entity_id,
            'entityType': entity_type
        }
        return self.session.post_file(Paths.ATTACH, file_path=file_path, params=params)

    def get_attachment_by_entity(self, entity_id, entity_type):
        """Get Attachments by Entity Id, Entity Type"""
        params = {
            'entityId': entity_id,
            'entityType': entity_type
        }
        return self.session.get(Paths.ATTACH_ENT, params=params)

    def get_attachment_file(self, attach_file_id, attachment_name=None):
        """Get Attachment file by Attachment file Id"""
        response = self.session.get(Paths.ATTACH_FILE.format(attach_file_id), return_raw=True)
        if attachment_name:
            with open(attachment_name, 'wb') as file:
                file.write(response.content)
        return response.content


class ZAPIResourceEndpoints(EndpointTemplate):
    """Following section describes the rest resources pertaining to ZAPIResource"""

    def get_zapi_module_status(self):
        """Get ZAPI Module Status"""
        return self.session.get(Paths.MOD_INFO)


class ZQLAutoCompleteResourceEndpoints(EndpointTemplate):
    """
    Following section describes rest resources (API's) pertaining to
    ExecutionFilteAutoCompleteResource
    """

    def get_zql_auto_complete_result(self, **params):
        """Get ZQL Auto Complete Result by Field Name, Field Value"""
        raise NotImplementedError


class SystemInfoResourceEndpoints(EndpointTemplate):
    """Following section describes the rest resources pertaining to SystemInfoResource"""

    def get_system_information(self):
        """Get System Information"""
        return self.session.get(Paths.SYS_INFO)


class FilterPickerResourceEndpoints(EndpointTemplate):
    """Following section describes the rest resources pertaining to FilterPickerResource"""

    def get_search_for_filter(self, **params):
        """Get Search For Filter"""
        raise NotImplementedError
