"""
Usage examples of Zephyr Squad Server API wrappers.
"""
import logging

from zephyr import ZephyrSquad

# Enable logging with level Debug for more verbosity
logging.basicConfig(level=logging.DEBUG)


# Specify your Jira context to operate with:
base_url = "https://jira.hosted.com/"

# Use the Jira certificate for TLS connections
session_params = {
    "verify": "<path-to-certificate>"
}

# Create an instance of Zephyr Squad
zsquad = ZephyrSquad(
    base_url=base_url,
    token="<token>",
    session_attrs=session_params
)

# Now we can start playing with the Zephyr API!

# Obtain a project's information
project_info = zsquad.actions.project.get_project_info("<project_key>")

# Obtain a project's versions/releases
project_versions = zsquad.api.util_resource.get_all_versions("<project_id>")

# Get the data of a testcase
test_case = zsquad.actions.test_cases.get_test_case("<case_key>", fields="id")

# Get the test steps from a testcase
test_steps = zsquad.api.teststep_resource.get_list_of_teststeps("<issue_id>")

# Get the information about a test cycle
test_cycle = zsquad.api.cycle_resource.get_cycle_information(cycle_id="<cycle_id>")

# Get the list of all test cycles for a specific release
test_cycles = zsquad.api.cycle_resource.get_list_of_cycle(project_id="<project_id>", versionId="<version_id>")

# Get all folders from a test cycle
test_cycle_folders = zsquad.api.cycle_resource.get_the_list_of_folder_for_a_cycle(cycle_id="<cycle_id>", project_id="<project_id>", version_id="<version_id>")

# Get all test executions from a test case
test_executions = zsquad.api.traceability_resource.get_list_of_search_execution_by_test(test_id_or_key="<test_id_or_key>")

# Create a new test case for a project
data = {
    "fields": {
        "assignee": {
            "name": "<jira_username>"
        },
        "description": "<case_description>"
    }
}
ret_data = zsquad.actions.test_cases.create_test_case(project_id="<project_id>", summary="<case_summary>", data=data)

# Execute ZQL search query
demo_query = "project = '<project_id>' AND cycleName = '<cycle_name>'"
zql_search_res = zsquad.api.execution_search_resource.execute_search_to_get_search_result(query=demo_query, maxRecords=200)

# Create a new test cycle for a project based on an existing test case
data = {
    "clonedCycleId": "<cycle_id>",
    "description": "<cycle_description>",
    "build": "",
    "startDate": "29/Nov/22",
    "endDate": "4/Dec/22",
    "environment": ""
}
ret_data = zsquad.api.cycle_resource.create_new_cycle(project_id="<project_id>", version_id="<version_id>", name="<cycle_name>", data=data)

# Create a new test folder for a test cycle
data = {
    "cycleId": 1508,  # it will be rewritten by the function
    "name": "<folder_name>",
    "description": "<folder_description>",
    "projectId": 10600,  # it will be rewritten by the function
    "versionId": -1,  # it will be rewritten by the function
    "clonedFolderId": -1
}
ret_data = zsquad.api.folder_resource.create_folder_under_cycle(project_id="<project_id>", version_id="<version_id>", cycle_id="<cycle_id>", data=data)

# Add a new test case for a test cycle
data = {
    "issues":["<case_key>"],
}
ret_data = zsquad.api.execution_resource.add_test_to_cycle(project_id="<project_id>", cycle_id="<cycle_id>", method="1", data=data)

# Obtain the execution details
exec_details = zsquad.api.execution_resource.get_execution_information(execution_id="<execution_id>")

# Obtain the execution steps from an execution
exec_steps = zsquad.api.step_result_resource.get_list_of_step_result(execution_id="<execution_id>")

# Update the status of an execution step
step_status = zsquad.api.step_result_resource.update_step_result_information(step_result_id="<execution_step_id>", status=2)

# Update the execution status
exec_status = zsquad.api.execution_resource.update_execution_details(execution_id="<execution_id>", status=2)

# Update a folder name and description
data = {
    "description": "<new_folder_decription>"
}
ret_data = zsquad.api.folder_resource.update_folder_information(project_id="<project_id>", version_id="<version_id>", cycle_id="<cycle_id>", folder_id="<folder_id>", name="<new_folder_name>")

# Delete 3 test executions
delete_status = zsquad.api.execution_resource.delete_bulk_execution(execution_id=["<exec_id_1>", "<exec_id_2>", "<exec_id_3>"])

# Show the progress of a job
job_status = zsquad.api.execution_resource.get_job_progress_status(job_progress_token="<job_progress_token>")

# Get a test step's detailed information
test_step = zsquad.api.teststep_resource.get_teststep_information(test_step_id="<test_step_id>", issue_id="<issue_id>")

# Add a attachment (for a execution result: entityId=executionId and entityType='Execution')
attach = zsquad.api.attachment_resource.add_attachment_into_entity(file_path="<file_path>", entity_id="<entity_id>", entity_type='<entity_type>')

# Add a assignee to a execution result
add_assignee = zsquad.api.execution_resource.add_assignee_to_execution(execution_id="<exec_id>", assignee="<username>")

# Create a test execution result in a test cycle
data = {
    "folderId": "<folder_id>"
}
ret_data = zsquad.api.execution_resource.create_new_execution(project_id="<project_id>", cycle_id="<cycle_id>", version_id="<version_id>", issue_id="<issue_id>", data=data)
