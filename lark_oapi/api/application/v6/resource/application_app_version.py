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
from lark_oapi.api.application.v6.model.contacts_range_suggest_application_app_version_request import ContactsRangeSuggestApplicationAppVersionRequest
from lark_oapi.api.application.v6.model.contacts_range_suggest_application_app_version_response import ContactsRangeSuggestApplicationAppVersionResponse
from lark_oapi.api.application.v6.model.get_application_app_version_request import GetApplicationAppVersionRequest
from lark_oapi.api.application.v6.model.get_application_app_version_response import GetApplicationAppVersionResponse
from lark_oapi.api.application.v6.model.list_application_app_version_request import ListApplicationAppVersionRequest
from lark_oapi.api.application.v6.model.list_application_app_version_response import ListApplicationAppVersionResponse
from lark_oapi.api.application.v6.model.patch_application_app_version_request import PatchApplicationAppVersionRequest
from lark_oapi.api.application.v6.model.patch_application_app_version_response import PatchApplicationAppVersionResponse


class ApplicationAppVersion(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def contacts_range_suggest(self, request: ContactsRangeSuggestApplicationAppVersionRequest, option: RequestOption = RequestOption()) -> ContactsRangeSuggestApplicationAppVersionResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ContactsRangeSuggestApplicationAppVersionResponse = JSON.unmarshal(str(resp.content, UTF_8), ContactsRangeSuggestApplicationAppVersionResponse)
        response.raw = resp

        return response

    def get(self, request: GetApplicationAppVersionRequest, option: RequestOption = RequestOption()) -> GetApplicationAppVersionResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: GetApplicationAppVersionResponse = JSON.unmarshal(str(resp.content, UTF_8), GetApplicationAppVersionResponse)
        response.raw = resp

        return response

    def list(self, request: ListApplicationAppVersionRequest, option: RequestOption = RequestOption()) -> ListApplicationAppVersionResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: ListApplicationAppVersionResponse = JSON.unmarshal(str(resp.content, UTF_8), ListApplicationAppVersionResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchApplicationAppVersionRequest, option: RequestOption = RequestOption()) -> PatchApplicationAppVersionResponse:
        # 鉴权、获取token
        verify(self.config, request, option)
        
        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)
        
        # 反序列化
        response: PatchApplicationAppVersionResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchApplicationAppVersionResponse)
        response.raw = resp

        return response

    
