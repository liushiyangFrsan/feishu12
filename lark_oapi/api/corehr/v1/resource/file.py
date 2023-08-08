# Code generated by Lark OpenAPI.

import io
from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from lark_oapi.core.utils import Files
from ..model.get_file_request import GetFileRequest
from ..model.get_file_response import GetFileResponse


class File(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def get(self, request: GetFileRequest, option: Optional[RequestOption] = None) -> GetFileResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 处理二进制流
        if resp.status_code == 200:
            response: GetFileResponse = GetFileResponse({})
            response.code = 0
            response.raw = resp
            response.file = io.BytesIO(resp.content)
            response.file_name = Files.parse_file_name(response.raw.header)
            return response

        # 反序列化
        response: GetFileResponse = JSON.unmarshal(str(resp.content, UTF_8), GetFileResponse)
        response.raw = resp

        return response
