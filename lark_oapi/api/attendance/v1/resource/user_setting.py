# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.modify_user_setting_request import ModifyUserSettingRequest
from ..model.modify_user_setting_response import ModifyUserSettingResponse
from ..model.query_user_setting_request import QueryUserSettingRequest
from ..model.query_user_setting_response import QueryUserSettingResponse


class UserSetting(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def modify(self, request: ModifyUserSettingRequest,
               option: Optional[RequestOption] = None) -> ModifyUserSettingResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ModifyUserSettingResponse = JSON.unmarshal(str(resp.content, UTF_8), ModifyUserSettingResponse)
        response.raw = resp

        return response

    def query(self, request: QueryUserSettingRequest,
              option: Optional[RequestOption] = None) -> QueryUserSettingResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QueryUserSettingResponse = JSON.unmarshal(str(resp.content, UTF_8), QueryUserSettingResponse)
        response.raw = resp

        return response
