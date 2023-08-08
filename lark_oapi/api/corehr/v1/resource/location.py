# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_location_request import CreateLocationRequest
from ..model.create_location_response import CreateLocationResponse
from ..model.delete_location_request import DeleteLocationRequest
from ..model.delete_location_response import DeleteLocationResponse
from ..model.get_location_request import GetLocationRequest
from ..model.get_location_response import GetLocationResponse
from ..model.list_location_request import ListLocationRequest
from ..model.list_location_response import ListLocationResponse


class Location(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateLocationRequest, option: Optional[RequestOption] = None) -> CreateLocationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateLocationResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateLocationResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteLocationRequest, option: Optional[RequestOption] = None) -> DeleteLocationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteLocationResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteLocationResponse)
        response.raw = resp

        return response

    def get(self, request: GetLocationRequest, option: Optional[RequestOption] = None) -> GetLocationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetLocationResponse = JSON.unmarshal(str(resp.content, UTF_8), GetLocationResponse)
        response.raw = resp

        return response

    def list(self, request: ListLocationRequest, option: Optional[RequestOption] = None) -> ListLocationResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListLocationResponse = JSON.unmarshal(str(resp.content, UTF_8), ListLocationResponse)
        response.raw = resp

        return response
