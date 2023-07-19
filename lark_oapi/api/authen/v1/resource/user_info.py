# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.authen.v1.model.get_user_info_request import GetUserInfoRequest
from lark_oapi.api.authen.v1.model.get_user_info_response import GetUserInfoResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class UserInfo(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def get(self, request: GetUserInfoRequest, option: RequestOption = RequestOption()) -> GetUserInfoResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetUserInfoResponse = JSON.unmarshal(str(resp.content, UTF_8), GetUserInfoResponse)
        response.raw = resp

        return response