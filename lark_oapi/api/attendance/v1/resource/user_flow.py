# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.batch_create_user_flow_request import BatchCreateUserFlowRequest
from ..model.batch_create_user_flow_response import BatchCreateUserFlowResponse
from ..model.get_user_flow_request import GetUserFlowRequest
from ..model.get_user_flow_response import GetUserFlowResponse
from ..model.query_user_flow_request import QueryUserFlowRequest
from ..model.query_user_flow_response import QueryUserFlowResponse


class UserFlow(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def batch_create(self, request: BatchCreateUserFlowRequest,
                     option: Optional[RequestOption] = None) -> BatchCreateUserFlowResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchCreateUserFlowResponse = JSON.unmarshal(str(resp.content, UTF_8), BatchCreateUserFlowResponse)
        response.raw = resp

        return response

    def get(self, request: GetUserFlowRequest, option: Optional[RequestOption] = None) -> GetUserFlowResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetUserFlowResponse = JSON.unmarshal(str(resp.content, UTF_8), GetUserFlowResponse)
        response.raw = resp

        return response

    def query(self, request: QueryUserFlowRequest, option: Optional[RequestOption] = None) -> QueryUserFlowResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QueryUserFlowResponse = JSON.unmarshal(str(resp.content, UTF_8), QueryUserFlowResponse)
        response.raw = resp

        return response
