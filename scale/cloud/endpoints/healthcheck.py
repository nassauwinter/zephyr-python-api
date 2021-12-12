from ...zephyr_session import ZephyrSession


class HealthcheckEndpoints:
    """Api wrapper for "Healthcheck" endpoints"""

    def __init__(self, session: ZephyrSession):
        self.session = session

    def get_health(self):
        """Check the health of this API

        :return: health check response body
        :rtype: dict
        """
        return self.session.get("healthcheck")
