# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetAgentSchedulesRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.agent_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetAgentSchedulesRequestBuilder":
        return GetAgentSchedulesRequestBuilder()


class GetAgentSchedulesRequestBuilder(object):

    def __init__(self, get_agent_schedules_request: GetAgentSchedulesRequest = GetAgentSchedulesRequest()) -> None:
        get_agent_schedules_request.http_method = HttpMethod.GET
        get_agent_schedules_request.uri = "/open-apis/helpdesk/v1/agents/:agent_id/schedules"
        get_agent_schedules_request.token_types = {AccessTokenType.TENANT}
        self._get_agent_schedules_request: GetAgentSchedulesRequest = get_agent_schedules_request

    def agent_id(self, agent_id: str) -> "GetAgentSchedulesRequestBuilder":
        self._get_agent_schedules_request.agent_id = agent_id
        self._get_agent_schedules_request.paths["agent_id"] = str(agent_id)
        return self

    def build(self) -> GetAgentSchedulesRequest:
        return self._get_agent_schedules_request
