# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_draft_request import CreateDraftRequest
from ..model.create_draft_response import CreateDraftResponse
from ..model.update_draft_request import UpdateDraftRequest
from ..model.update_draft_response import UpdateDraftResponse


class Draft(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateDraftRequest, option: Optional[RequestOption] = None) -> CreateDraftResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateDraftResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateDraftResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateDraftRequest, option: Optional[RequestOption] = None) -> UpdateDraftResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateDraftResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateDraftResponse)
        response.raw = resp

        return response
