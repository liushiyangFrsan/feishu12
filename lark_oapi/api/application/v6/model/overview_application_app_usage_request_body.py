# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class OverviewApplicationAppUsageRequestBody(object):
    _types = {
        "date": str,
        "cycle_type": int,
        "department_id": str,
        "ability": str,
    }

    def __init__(self, d):
        self.date: Optional[str] = None
        self.cycle_type: Optional[int] = None
        self.department_id: Optional[str] = None
        self.ability: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OverviewApplicationAppUsageRequestBodyBuilder":
        return OverviewApplicationAppUsageRequestBodyBuilder()


class OverviewApplicationAppUsageRequestBodyBuilder(object):
    def __init__(self, overview_application_app_usage_request_body: OverviewApplicationAppUsageRequestBody = OverviewApplicationAppUsageRequestBody({})) -> None:
        self._overview_application_app_usage_request_body: OverviewApplicationAppUsageRequestBody = overview_application_app_usage_request_body
    
    def date(self, date: str) -> "OverviewApplicationAppUsageRequestBodyBuilder":
        self._overview_application_app_usage_request_body.date = date
        return self
    
    def cycle_type(self, cycle_type: int) -> "OverviewApplicationAppUsageRequestBodyBuilder":
        self._overview_application_app_usage_request_body.cycle_type = cycle_type
        return self
    
    def department_id(self, department_id: str) -> "OverviewApplicationAppUsageRequestBodyBuilder":
        self._overview_application_app_usage_request_body.department_id = department_id
        return self
    
    def ability(self, ability: str) -> "OverviewApplicationAppUsageRequestBodyBuilder":
        self._overview_application_app_usage_request_body.ability = ability
        return self
    
    def build(self) -> "OverviewApplicationAppUsageRequestBody":
        return self._overview_application_app_usage_request_body