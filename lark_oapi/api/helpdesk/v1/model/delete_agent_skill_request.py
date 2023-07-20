# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteAgentSkillRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.agent_skill_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteAgentSkillRequestBuilder":
        return DeleteAgentSkillRequestBuilder()


class DeleteAgentSkillRequestBuilder(object):

    def __init__(self, delete_agent_skill_request: DeleteAgentSkillRequest = DeleteAgentSkillRequest()) -> None:
        delete_agent_skill_request.http_method = HttpMethod.DELETE
        delete_agent_skill_request.uri = "/open-apis/helpdesk/v1/agent_skills/:agent_skill_id"
        delete_agent_skill_request.token_types = {AccessTokenType.USER}
        self._delete_agent_skill_request: DeleteAgentSkillRequest = delete_agent_skill_request

    def agent_skill_id(self, agent_skill_id: str) -> "DeleteAgentSkillRequestBuilder":
        self._delete_agent_skill_request.agent_skill_id = agent_skill_id
        self._delete_agent_skill_request.paths["agent_skill_id"] = str(agent_skill_id)
        return self

    def build(self) -> DeleteAgentSkillRequest:
        return self._delete_agent_skill_request
