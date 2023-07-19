# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.search.v2.model.create_message_request import CreateMessageRequest
from lark_oapi.api.search.v2.model.create_message_response import CreateMessageResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class Message(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def create(self, request: CreateMessageRequest, option: RequestOption = RequestOption()) -> CreateMessageResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateMessageResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateMessageResponse)
        response.raw = resp

        return response