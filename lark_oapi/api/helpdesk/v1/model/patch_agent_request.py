# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .patch_agent_request_body import PatchAgentRequestBody


class PatchAgentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.agent_id: Optional[str] = None
        self.request_body: Optional[PatchAgentRequestBody] = None

    @staticmethod
    def builder() -> "PatchAgentRequestBuilder":
        return PatchAgentRequestBuilder()


class PatchAgentRequestBuilder(object):

    def __init__(self, patch_agent_request: PatchAgentRequest = PatchAgentRequest()) -> None:
        patch_agent_request.http_method = HttpMethod.PATCH
        patch_agent_request.uri = "/open-apis/helpdesk/v1/agents/:agent_id"
        patch_agent_request.token_types = {AccessTokenType.USER}
        self._patch_agent_request: PatchAgentRequest = patch_agent_request

    def agent_id(self, agent_id: str) -> "PatchAgentRequestBuilder":
        self._patch_agent_request.agent_id = agent_id
        self._patch_agent_request.paths["agent_id"] = str(agent_id)
        return self

    def request_body(self, request_body: PatchAgentRequestBody) -> "PatchAgentRequestBuilder":
        self._patch_agent_request.request_body = request_body
        self._patch_agent_request.body = request_body
        return self

    def build(self) -> PatchAgentRequest:
        return self._patch_agent_request
