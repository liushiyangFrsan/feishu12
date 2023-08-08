# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.copy_app_dashboard_request import CopyAppDashboardRequest
from ..model.copy_app_dashboard_response import CopyAppDashboardResponse
from ..model.list_app_dashboard_request import ListAppDashboardRequest
from ..model.list_app_dashboard_response import ListAppDashboardResponse


class AppDashboard(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def copy(self, request: CopyAppDashboardRequest,
             option: Optional[RequestOption] = None) -> CopyAppDashboardResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CopyAppDashboardResponse = JSON.unmarshal(str(resp.content, UTF_8), CopyAppDashboardResponse)
        response.raw = resp

        return response

    def list(self, request: ListAppDashboardRequest,
             option: Optional[RequestOption] = None) -> ListAppDashboardResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListAppDashboardResponse = JSON.unmarshal(str(resp.content, UTF_8), ListAppDashboardResponse)
        response.raw = resp

        return response
