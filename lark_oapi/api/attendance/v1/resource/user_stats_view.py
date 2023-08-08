# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.query_user_stats_view_request import QueryUserStatsViewRequest
from ..model.query_user_stats_view_response import QueryUserStatsViewResponse
from ..model.update_user_stats_view_request import UpdateUserStatsViewRequest
from ..model.update_user_stats_view_response import UpdateUserStatsViewResponse


class UserStatsView(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def query(self, request: QueryUserStatsViewRequest,
              option: Optional[RequestOption] = None) -> QueryUserStatsViewResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QueryUserStatsViewResponse = JSON.unmarshal(str(resp.content, UTF_8), QueryUserStatsViewResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateUserStatsViewRequest,
               option: Optional[RequestOption] = None) -> UpdateUserStatsViewResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateUserStatsViewResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateUserStatsViewResponse)
        response.raw = resp

        return response
