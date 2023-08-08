# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.batch_query_file_comment_request import BatchQueryFileCommentRequest
from ..model.batch_query_file_comment_response import BatchQueryFileCommentResponse
from ..model.create_file_comment_request import CreateFileCommentRequest
from ..model.create_file_comment_response import CreateFileCommentResponse
from ..model.get_file_comment_request import GetFileCommentRequest
from ..model.get_file_comment_response import GetFileCommentResponse
from ..model.list_file_comment_request import ListFileCommentRequest
from ..model.list_file_comment_response import ListFileCommentResponse
from ..model.patch_file_comment_request import PatchFileCommentRequest
from ..model.patch_file_comment_response import PatchFileCommentResponse


class FileComment(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def batch_query(self, request: BatchQueryFileCommentRequest,
                    option: Optional[RequestOption] = None) -> BatchQueryFileCommentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchQueryFileCommentResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 BatchQueryFileCommentResponse)
        response.raw = resp

        return response

    def create(self, request: CreateFileCommentRequest,
               option: Optional[RequestOption] = None) -> CreateFileCommentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateFileCommentResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateFileCommentResponse)
        response.raw = resp

        return response

    def get(self, request: GetFileCommentRequest, option: Optional[RequestOption] = None) -> GetFileCommentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetFileCommentResponse = JSON.unmarshal(str(resp.content, UTF_8), GetFileCommentResponse)
        response.raw = resp

        return response

    def list(self, request: ListFileCommentRequest, option: Optional[RequestOption] = None) -> ListFileCommentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListFileCommentResponse = JSON.unmarshal(str(resp.content, UTF_8), ListFileCommentResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchFileCommentRequest,
              option: Optional[RequestOption] = None) -> PatchFileCommentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchFileCommentResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchFileCommentResponse)
        response.raw = resp

        return response
