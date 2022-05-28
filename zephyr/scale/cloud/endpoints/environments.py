from ...zephyr_session import ZephyrSession


class EnvironmentEndpoints:
    """Api wrapper for "Environment" endpoints"""

    def __init__(self, session: ZephyrSession):
        self.session = session

    def get_environments(self, **kwargs):
        return self.session.get_paginated("environments", params=kwargs)

    def get_environment(self, environment_id):
        return self.session.get("environments/{}".format(environment_id))
