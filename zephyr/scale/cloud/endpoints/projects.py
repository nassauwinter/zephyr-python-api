from zephyr.scale.zephyr_scale_session import ZephyrScaleSession


class ProjectEndpoints:
    """Api wrapper for "Project" endpoints"""

    def __init__(self, session: ZephyrScaleSession):
        self.session = session

    def get_projects(self):
        """Returns all projects"""
        return self.session.get_paginated("projects")

    def get_project(self, project_id_or_key):
        """Returns a project for the given ID or key"""
        return self.session.get(f"projects/{project_id_or_key}")
