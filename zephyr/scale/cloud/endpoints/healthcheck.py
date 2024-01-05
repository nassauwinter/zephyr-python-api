from zephyr.scale.zephyr_scale_session import ZephyrScaleSession


class HealthcheckEndpoints:
    """Api wrapper for "Healthcheck" endpoints"""

    def __init__(self, session: ZephyrScaleSession):
        self.session = session

    def get_health(self):
        """Check the health of this API

        :return: health check response body
        :rtype: dict
        """
        return self.session.get("healthcheck")
