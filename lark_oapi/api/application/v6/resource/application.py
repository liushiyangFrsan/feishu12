# Code generated by Lark OpenAPI.

import io
from typing import *
from typing import IO
from lark_oapi.core.const import UTF_8, CONTENT_TYPE
from lark_oapi.core import JSON
from lark_oapi.core.token import verify
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.utils import Files
from requests_toolbelt import MultipartEncoder
from lark_oapi.api.application.v6.model.contacts_range_configuration_application_request import ContactsRangeConfigurationApplicationRequest
from lark_oapi.api.application.v6.model.contacts_range_configuration_application_response import ContactsRangeConfigurationApplicationResponse
from lark_oapi.api.application.v6.model.get_application_request import GetApplicationRequest
from lark_oapi.api.application.v6.model.get_application_response import GetApplicationResponse
from lark_oapi.api.application.v6.model.patch_application_request import PatchApplicationRequest
from lark_oapi.api.application.v6.model.patch_application_response import PatchApplicationResponse
from lark_oapi.api.application.v6.model.underauditlist_application_request import UnderauditlistApplicationRequest
from lark_oapi.api.application.v6.model.underauditlist_application_response import UnderauditlistApplicationResponse


class Application(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def contacts_range_configuration(self, request: ContactsRangeConfigurationApplicationRequest, option: RequestOption = RequestOption()) -> ContactsRangeConfigurationApplicationResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ContactsRangeConfigurationApplicationResponse = JSON.unmarshal(str(resp.content, UTF_8), ContactsRangeConfigurationApplicationResponse)
        response.raw = resp

        return response

    def get(self, request: GetApplicationRequest, option: RequestOption = RequestOption()) -> GetApplicationResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: GetApplicationResponse = JSON.unmarshal(str(resp.content, UTF_8), GetApplicationResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchApplicationRequest, option: RequestOption = RequestOption()) -> PatchApplicationResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: PatchApplicationResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchApplicationResponse)
        response.raw = resp

        return response

    def underauditlist(self, request: UnderauditlistApplicationRequest, option: RequestOption = RequestOption()) -> UnderauditlistApplicationResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: UnderauditlistApplicationResponse = JSON.unmarshal(str(resp.content, UTF_8), UnderauditlistApplicationResponse)
        response.raw = resp

        return response

    
