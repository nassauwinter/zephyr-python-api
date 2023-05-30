import logging

from zephyr.squad.zephyr_squad_session import ZephyrSquadSession
from zephyr.squad.server import endpoints


# pylint: disable=missing-function-docstring
class ServerApiWrapper:
    """Zephyr Squad Server Api wrapper"""
    def __init__(self, session: ZephyrSquadSession):
        self.session = session
        self.logger = logging.getLogger(__name__)

    @property
    def chart_resource(self):
        return endpoints.ChartResourceEndpoints(self.session)

    @property
    def execution_search_resource(self):
        return endpoints.ExecutionSearchResourceEndpoints(self.session)

    @property
    def zql_filter_resource(self):
        return endpoints.ZQLFilterResourceEndpoints(self.session)

    @property
    def cycle_resource(self):
        return endpoints.CycleResourceEndpoints(self.session)

    @property
    def znav_resource(self):
        return endpoints.ZNavResourceEndpoints(self.session)

    @property
    def license_resource(self):
        return endpoints.LicenseResourceEndpoints(self.session)

    @property
    def preference_resource(self):
        return endpoints.PreferenceResourceEndpoints(self.session)

    @property
    def step_result_resource(self):
        return endpoints.StepResultResourceEndpoints(self.session)

    @property
    def traceability_resource(self):
        return endpoints.TraceabilityResourceEndpoints(self.session)

    @property
    def testcase_resource(self):
        return endpoints.TestcaseResourceEndpoints(self.session)

    @property
    def util_resource(self):
        return endpoints.UtilResourceEndpoints(self.session)

    @property
    def folder_resource(self):
        return endpoints.FolderResourceEndpoints(self.session)

    @property
    def execution_resource(self):
        return endpoints.ExecutionResourceEndpoints(self.session)

    @property
    def issue_picker_resource(self):
        return endpoints.IssuePickerResourceEndpoints(self.session)

    @property
    def audit_resource(self):
        return endpoints.AuditResourceEndpoints(self.session)

    @property
    def teststep_resource(self):
        return endpoints.TeststepResourceEndpoints(self.session)

    @property
    def attachment_resource(self):
        return endpoints.AttachmentResourceEndpoints(self.session)

    @property
    def zapi_resource(self):
        return endpoints.ZAPIResourceEndpoints(self.session)

    @property
    def zql_autocomplete_resource(self):
        return endpoints.ZQLAutoCompleteResourceEndpoints(self.session)

    @property
    def systeminfo_resource(self):
        return endpoints.SystemInfoResourceEndpoints(self.session)

    @property
    def filter_picker_resource(self):
        return endpoints.FilterPickerResourceEndpoints(self.session)
