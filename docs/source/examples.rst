Examples
=============

Authentication
-------------

Zephyr Cloud auth:

.. code-block:: python

    from zephyr import ZephyrScale
    zscale = ZephyrScale(token=<your_token>)

Zephyr Server/Data Center (TM4J) auth:

.. code-block:: python

    from zephyr import ZephyrScale
    # Auth can be made with Jira token
    auth = {"token": "<your_jira_token>"}
    # or with login and password (suggest using get_pass)
    auth = {"username": "<your_login>", "password": "<your_password>"}
    # or even session cookie dict
    auth = {"cookies": "<session_cookie_dict>"}
    zscale = ZephyrScale.server_api(base_url=<your_base_url>, **auth)

Usage
-------------

Then it is possible to interact with api wrappers:

.. code-block:: python

    zapi = zscale.api
    # Get all test cases
    all_test_cases = zapi.test_cases.get_test_cases()
    # Get a single test case by its id
    test_case = zapi.test_cases.get_test_case("<test_case_id>")
    # Create a test case
    creation_result = zapi.test_cases.create_test_case("<project_key>", "test_case_name")
