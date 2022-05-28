from ...zephyr_session import ZephyrSession


class FolderEndpoints:
    """Api wrapper for "Folder" endpoints"""

    def __init__(self, session: ZephyrSession):
        self.session = session

    def get_folders(self, **kwargs):
        return self.session.get_paginated("folders", params=kwargs)

    def create_folder(self, name, project_key, folder_type, **kwargs):
        json = {"name": name,
                "projectKey": project_key,
                "folderType": folder_type}
        json.update(kwargs)
        return self.session.post("folders", json=json)

    def get_folder(self, folder_id):
        return self.session.get("folders/{}".format(folder_id))
