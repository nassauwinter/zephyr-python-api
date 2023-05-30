"""
Usage examples of Zephyr Scale Server API wrappers.
"""
import logging

from zephyr import ZephyrScale


# Enable logging with level Debug for more verbosity
logging.basicConfig(level=logging.DEBUG)


# Specify your Jira context to operate with:
base_url = "https://http://localhost:2990/jira/rest/atm/1.0/"


# Deside the type of authorization. It could be a token, username/password or cookies
auth = {"token": "<your_jira_token>"}
# auth = {"username": "<your_username>", "password": "your_pass"}
# auth = {"cookies": "<your_cookie_dict>"}

# Create an instance of Zephyr Scale
zscale = ZephyrScale.server_api(base_url=base_url, **auth)


# Now we can start playing with the Zephyr API!
test_cases = zscale.api.test_cases

# Get a test case:
case_data = test_cases.get_test_case("<your_case_id>")

# Create a test case:
creation_data = test_cases.create_test_case("<your_project_key>", "Test case name")

# Update a test case:
test_script = {
    "type": "STEP_BY_STEP",
    "steps": [
      {
        "description": "Description for the step 1",
        "testData": "Some test data",
        "expectedResult": "Expectations"
      },
      {
        "description": "Step 2 description",
        "testData": "Some more test data",
        "expectedResult": "Expected result for the step 2"
      }]}
update_data = test_cases.update_test_case("<your_case_id>",
                                          objective=f"New_test_objective",
                                          testScript=test_script)

# Delete a test case:
deleted = test_cases.delete_test_case("<case_id_you_don't_need_anymore>")

# Get test case attachments:
attachments = test_cases.get_attachments("<your_case_id>")

# Create a test case attachment (upload):
upload_result = test_cases.create_attachment("<your_case_id>", "path_to_attachment_file")

# Get the latest execution result for the test case:
execution_data = test_cases.get_latest_result("<your_case_id>")

# Get attachments for a specified step:
test_cases.get_step_attachments("<your_case_id>", "<step_id>")

# Create an attachment for step:
test_cases.create_step_attachment("<your_case_id>", "<step_id>", "path_to_attachment_file")

# Search test cases with JQL:
search = test_cases.search_cases(query='projectKey = "<your_awesome_porojects_key>"')
