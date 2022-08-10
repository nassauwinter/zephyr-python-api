from ...zephyr_session import ZephyrSession


class LinkEndpoints:
    """Api wrapper for "Link" endpoints"""

    def __init__(self, session: ZephyrSession):
        self.session = session

    def delete_link(self, link_id):
        """Deletes a link for the given ID.

        :param link_id: The id of a link to delete
        :type link_id: int
        :return: response body
        :rtype: dict
        """
        return self.session.delete(f"links/{link_id}")
