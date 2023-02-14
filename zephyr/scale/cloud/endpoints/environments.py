from ...zephyr_session import ZephyrSession


class EnvironmentEndpoints:
    """Api wrapper for "Environment" endpoints"""

    def __init__(self, session: ZephyrSession):
        self.session = session

    def get_environments(self, **kwargs):
        """Returns all environments"""
        return self.session.get_paginated("environments", params=kwargs)

    def get_environment(self, environment_id):
        """Returns an environment for the given ID"""
        return self.session.get(f"environments/{environment_id}")
