# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.get_work_city_request import GetWorkCityRequest
from ..model.get_work_city_response import GetWorkCityResponse
from ..model.list_work_city_request import ListWorkCityRequest
from ..model.list_work_city_response import ListWorkCityResponse


class WorkCity(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def get(self, request: GetWorkCityRequest, option: Optional[RequestOption] = None) -> GetWorkCityResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetWorkCityResponse = JSON.unmarshal(str(resp.content, UTF_8), GetWorkCityResponse)
        response.raw = resp

        return response

    def list(self, request: ListWorkCityRequest, option: Optional[RequestOption] = None) -> ListWorkCityResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListWorkCityResponse = JSON.unmarshal(str(resp.content, UTF_8), ListWorkCityResponse)
        response.raw = resp

        return response
