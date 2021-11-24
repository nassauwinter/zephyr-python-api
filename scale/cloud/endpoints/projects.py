from ...zephyr_session import ZephyrSession


class ProjectEndpoints:
    """Api wrapper for "Project" endpoints"""

    def __init__(self, session: ZephyrSession):
        self.session = session

    def get_projects(self):
        return self.session.get_paginated("projects")

    def get_project(self, project_id_or_key):
        return self.session.get(f"projects/{project_id_or_key}")
