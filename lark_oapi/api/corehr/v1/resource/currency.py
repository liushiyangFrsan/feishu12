# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.get_currency_request import GetCurrencyRequest
from ..model.get_currency_response import GetCurrencyResponse
from ..model.list_currency_request import ListCurrencyRequest
from ..model.list_currency_response import ListCurrencyResponse


class Currency(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def get(self, request: GetCurrencyRequest, option: Optional[RequestOption] = None) -> GetCurrencyResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetCurrencyResponse = JSON.unmarshal(str(resp.content, UTF_8), GetCurrencyResponse)
        response.raw = resp

        return response

    def list(self, request: ListCurrencyRequest, option: Optional[RequestOption] = None) -> ListCurrencyResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListCurrencyResponse = JSON.unmarshal(str(resp.content, UTF_8), ListCurrencyResponse)
        response.raw = resp

        return response
