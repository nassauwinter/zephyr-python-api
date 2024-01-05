from zephyr.scale.zephyr_scale_session import ZephyrScaleSession


class FolderEndpoints:
    """Api wrapper for "Folder" endpoints"""

    def __init__(self, session: ZephyrScaleSession):
        self.session = session

    def get_folders(self, **kwargs):
        """Returns all folders"""
        return self.session.get_paginated("folders", params=kwargs)

    def create_folder(self, name, project_key, folder_type, **kwargs):
        """Creates a folder"""
        json = {"name": name,
                "projectKey": project_key,
                "folderType": folder_type}
        json.update(kwargs)
        return self.session.post("folders", json=json)

    def get_folder(self, folder_id):
        """Returns a folder for the given ID"""
        return self.session.get(f"folders/{folder_id}")
