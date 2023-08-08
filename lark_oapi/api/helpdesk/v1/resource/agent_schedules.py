# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.delete_agent_schedules_request import DeleteAgentSchedulesRequest
from ..model.delete_agent_schedules_response import DeleteAgentSchedulesResponse
from ..model.get_agent_schedules_request import GetAgentSchedulesRequest
from ..model.get_agent_schedules_response import GetAgentSchedulesResponse
from ..model.patch_agent_schedules_request import PatchAgentSchedulesRequest
from ..model.patch_agent_schedules_response import PatchAgentSchedulesResponse


class AgentSchedules(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def delete(self, request: DeleteAgentSchedulesRequest,
               option: Optional[RequestOption] = None) -> DeleteAgentSchedulesResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteAgentSchedulesResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteAgentSchedulesResponse)
        response.raw = resp

        return response

    def get(self, request: GetAgentSchedulesRequest,
            option: Optional[RequestOption] = None) -> GetAgentSchedulesResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetAgentSchedulesResponse = JSON.unmarshal(str(resp.content, UTF_8), GetAgentSchedulesResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchAgentSchedulesRequest,
              option: Optional[RequestOption] = None) -> PatchAgentSchedulesResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchAgentSchedulesResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchAgentSchedulesResponse)
        response.raw = resp

        return response
