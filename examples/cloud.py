"""
Examples for the Zephyr Scale in Jira cloud.
"""
import logging

from zephyr import ZephyrScale


# Some logging to see what is happening
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Now initialize the Zephyr Scale object with the token
# How to generate a token:
# https://support.smartbear.com/zephyr-scale-cloud/docs/en/rest-api/generating-api-access-tokens.html
token = "my super secret token"

zsc = ZephyrScale(token=token)


# Test Cases
# Get all the test cases. Even from different projects.
all_cases = list(zsc.api.test_cases.get_test_cases())

# Or from a specific project.
tpr_cases = list(zsc.api.test_cases.get_test_cases("TPR"))

# Create a test case in a project. Let it be TPR.
created_case_data = zsc.api.test_cases.create_test_case("TPR",
                                                        "Test the pen draws a line",
                                                        objective="The pen could draw a line on a sheet",
                                                        priorityName="Critical")

# Get a test case by its key.
test_case = zsc.api.test_cases.get_test_case("TPR-T1")

# Update a test case.
updated_test = zsc.api.test_cases.update_test_case("TPR-T1",  # case key
                                                   1,  # case id
                                                   "Test the pen draws a pink line",  # case name
                                                   10005,  # project id
                                                   10002,  # priority id
                                                   10000,  # status id
                                                   customFields={'Automated test': False, 'Framework': None})

# Get the links of a test case.
links = zsc.api.test_cases.get_links("TPR-T1")

# Create a link to an issue.
link_added = zsc.api.test_cases.create_issue_links("TPR-T1", 10001)

# Create a web link.
web_link_added = zsc.api.test_cases.create_web_links(
    "TPR-T1", "https://support.smartbear.com/zephyr-scale-cloud/api-docs/#tag/Test-Cases")

# Get the versions of a test case.
versions = list(zsc.api.test_cases.get_versions("TPR-T1"))

# Get a specific version of a test case.
ver_1_0 = zsc.api.test_cases.get_version("TPR-T1", 1)

# Get the test script of a test case.
script = zsc.api.test_cases.get_test_script("TPR-T1")

# Create a plain text test script.
plain_script = zsc.api.test_cases.create_test_script("TPR-T2",
                                                     "plain",
                                                     "1. Take the pen\n2. Draw a line\nCheck if it is blue and narrow")
# Or create a BDD test script.
bdd_script = zsc.api.test_cases.create_test_script("TPA-T3",
                                                   "bdd",
                                                   "Given there is a blue pen\n"
                                                   "And I have a sheet of white paper\n"
                                                   "When I draw a line with the pen\n"
                                                   "Then it should be blue and narrow")

# Get the test steps of a test case.
test_steps = list(zsc.api.test_cases.get_test_steps("TPR-T4"))

# Append a step to the test case.
step_added = zsc.api.test_cases.post_test_steps("TPA-T4",
                                                mode="APPEND",
                                                items=[{"inline": {"description": "Appended step"}}])
# Or overwrite the steps.
steps_overwrite = zsc.api.test_cases.post_test_steps("TPA-T4",
                                                     mode="OVERWRITE",
                                                     items=[{"inline": {"description": "Take a blue pen from a drawer",
                                                                        "expectedResult": "The pen is blue"}},
                                                            {"inline": {"description": "Draw a line on a sheet",
                                                                        "expectedResult": "The line is blue"}}])
