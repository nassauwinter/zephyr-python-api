from ...zephyr_session import ZephyrSession


class PriorityEndpoints:
    """Api wrapper for "Priority" endpoints"""

    def __init__(self, session: ZephyrSession):
        self.session = session

    def get_priorities(self, **kwargs):
        """Returns all priorities"""
        return self.session.get_paginated("priorities", params=kwargs)

    def get_priority(self, priority_id):
        """Returns a priority for the given ID"""
        return self.session.get(f"priorities/{priority_id}")
