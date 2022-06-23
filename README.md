# Zephyr-python-api

### Project description
This is a wrapper for Zephyr Scale (TM4J) REST API. This means you can interact with Zephyr Scale without GUI in a browser!

NOTE: Currently only Scale Cloud wrappers are implemented. 

To be done:
* Scale Server wrappers implementations
* Usage examples

### Installation

```
pip install zephyr-python-api
```

### Example usage

Zephyr Cloud auth:
```
from zephyr import ZephyrScale

zscale = ZephyrScale(token=<your_token>)
```

Zephyr Server (TM4J) auth:
```
from zephyr import API_V1, ZephyrScale

# Auth can be made with Jira token
auth = {"token": "<your_jira_token>"}

# or with login and password (suggest using get_pass)
auth = {"username": "<your_login>", "password": "<your_password>"}

# or even session cookie dict
auth = {"cookies": "<session_cookie_dict>"}

zscale = ZephyrScale(api=API_V1, base_url=<your_base_url>, **auth)
```

Then it is possible to interact with api wrappers:
```
zapi = zscale.api

all_test_cases = zapi.test_cases.get_test_cases()
```


### License

This library is licensed under the Apache 2.0 License.

### Links

[Zephyr Scale Cloud API docs](https://support.smartbear.com/zephyr-scale-cloud/api-docs/)

[Zephyr Scale Server API docs](https://support.smartbear.com/zephyr-scale-server/api-docs/v1/)