from urllib.parse import urlparse, parse_qs
from zephyr.common.zephyr_session import ZephyrSession


class ZephyrScaleSession(ZephyrSession):
    """
    Zephyr Scale basic session object.

    :param base_url: url to make requests to
    :param token: auth token
    :param username: username
    :param password: password
    :param cookies: cookie dict

    :keyword session_attrs: a dict with session attrs to be set as keys and their values
    """

    def get_paginated(self, endpoint, params=None):
        """Get paginated data"""
        self.logger.debug(f"Get paginated data from endpoint={endpoint} and params={params}")
        if params is None:
            params = {}

        while True:
            response = self.get(endpoint, params=params)
            if "values" not in response:
                return
            for value in response.get("values", []):
                yield value
            if response.get("isLast") is True:
                break
            params_str = urlparse(response.get("next")).query
            params.update(parse_qs(params_str))
        return

    def post_file(self, endpoint: str, file_path: str, to_files=None, **kwargs):
        """
        Post wrapper to send a file. Handles single file opening,
        sending its content and closing
        """
        with open(file_path, "rb") as file:
            files = {"file": file}

            if to_files:
                files.update(to_files)

            return self._request("post", endpoint, files=files, **kwargs)
