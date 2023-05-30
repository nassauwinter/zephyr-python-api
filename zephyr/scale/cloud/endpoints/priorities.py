from zephyr.scale.zephyr_scale_session import ZephyrScaleSession


class PriorityEndpoints:
    """Api wrapper for "Priority" endpoints"""

    def __init__(self, session: ZephyrScaleSession):
        self.session = session

    def get_priorities(self, **kwargs):
        """Returns all priorities"""
        return self.session.get_paginated("priorities", params=kwargs)

    def get_priority(self, priority_id):
        """Returns a priority for the given ID"""
        return self.session.get(f"priorities/{priority_id}")
