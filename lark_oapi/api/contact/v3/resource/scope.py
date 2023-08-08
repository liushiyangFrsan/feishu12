# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.list_scope_request import ListScopeRequest
from ..model.list_scope_response import ListScopeResponse


class Scope(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def list(self, request: ListScopeRequest, option: Optional[RequestOption] = None) -> ListScopeResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListScopeResponse = JSON.unmarshal(str(resp.content, UTF_8), ListScopeResponse)
        response.raw = resp

        return response
