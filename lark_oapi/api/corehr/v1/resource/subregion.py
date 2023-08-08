# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.get_subregion_request import GetSubregionRequest
from ..model.get_subregion_response import GetSubregionResponse
from ..model.list_subregion_request import ListSubregionRequest
from ..model.list_subregion_response import ListSubregionResponse


class Subregion(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def get(self, request: GetSubregionRequest, option: Optional[RequestOption] = None) -> GetSubregionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetSubregionResponse = JSON.unmarshal(str(resp.content, UTF_8), GetSubregionResponse)
        response.raw = resp

        return response

    def list(self, request: ListSubregionRequest, option: Optional[RequestOption] = None) -> ListSubregionResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListSubregionResponse = JSON.unmarshal(str(resp.content, UTF_8), ListSubregionResponse)
        response.raw = resp

        return response
