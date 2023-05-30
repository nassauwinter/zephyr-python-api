from zephyr.common.zephyr_session import ZephyrSession

class ZephyrSquadSession(ZephyrSession):
    """
    Zephyr Squad basic session object.

    :param base_url: url to make requests to
    :param token: auth token
    :param username: username
    :param password: password
    :param cookies: cookie dict

    :keyword session_attrs: a dict with session attrs to be set as keys and their values
    """

    def _paginated_test_label(self, endpoint, params):
        max_records = params.get("maxRecords") if params.get("maxRecords") else 10
        remove_no_labels = False
        while True:
            response = self.get(endpoint, params=params)
            if "values" not in response:
                return
            for value in response.get("values"):
                if remove_no_labels and value.get('name') == 'No Label':
                    continue
                remove_no_labels = True
                yield value
            if len(response.get("values")) + params.get("offset", 0) >= response.get("totalCount"):
                break

            if params.get("offset"):
                new_offset = params['offset'] + max_records
            else:
                new_offset = max_records
            params.update(offset=new_offset)

    def _paginated_execution(self, endpoint, params):
        while True:
            response = self.get(endpoint, params=params)
            if "executions" not in response or not response.get("executions"):
                return
            for execution in response.get("executions"):
                yield execution
            if response.get("linksNew")[-1] == response.get("currentIndex") or \
                response.get("maxResultAllowed") + response.get("offset", 0) \
                    >= response.get("totalCount"):
                break

            if params.get("offset"):
                new_offset = params['offset'] + response.get("maxResultAllowed")
            else:
                new_offset = response.get("maxResultAllowed")
            params.update(offset=new_offset)

    def get_paginated(self, endpoint, query_type, params=None):
        """Get paginated data"""
        available_types = [ "execution", "test-label" ]
        if query_type not in available_types:
            raise AttributeError(
                f"{query_type} is not a valid query type! Available: {','.join(available_types)}"
            )

        self.logger.debug(f"Get paginated data from endpoint={endpoint} and params={params}")
        if params is None:
            params = {}

        if query_type == "execution":
            return self._paginated_execution(endpoint, params)
        return self._paginated_test_label(endpoint, params)

    def post_file(self, endpoint: str, file_path: str, to_files=None, **kwargs):
        """
        Post wrapper to send a file. Handles single file opening,
        sending its content and closing
        """
        with open(file_path, "rb") as file:
            content_type = "multipart/form-data"
            files = {'file': (file_path, file, content_type)}

            if to_files:
                files.update(to_files)

            return self._request("post", endpoint, files=files, **kwargs)
