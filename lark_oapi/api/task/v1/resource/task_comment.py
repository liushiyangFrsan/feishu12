# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_task_comment_request import CreateTaskCommentRequest
from ..model.create_task_comment_response import CreateTaskCommentResponse
from ..model.delete_task_comment_request import DeleteTaskCommentRequest
from ..model.delete_task_comment_response import DeleteTaskCommentResponse
from ..model.get_task_comment_request import GetTaskCommentRequest
from ..model.get_task_comment_response import GetTaskCommentResponse
from ..model.list_task_comment_request import ListTaskCommentRequest
from ..model.list_task_comment_response import ListTaskCommentResponse
from ..model.update_task_comment_request import UpdateTaskCommentRequest
from ..model.update_task_comment_response import UpdateTaskCommentResponse


class TaskComment(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateTaskCommentRequest,
               option: Optional[RequestOption] = None) -> CreateTaskCommentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateTaskCommentResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateTaskCommentResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteTaskCommentRequest,
               option: Optional[RequestOption] = None) -> DeleteTaskCommentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteTaskCommentResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteTaskCommentResponse)
        response.raw = resp

        return response

    def get(self, request: GetTaskCommentRequest, option: Optional[RequestOption] = None) -> GetTaskCommentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetTaskCommentResponse = JSON.unmarshal(str(resp.content, UTF_8), GetTaskCommentResponse)
        response.raw = resp

        return response

    def list(self, request: ListTaskCommentRequest, option: Optional[RequestOption] = None) -> ListTaskCommentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListTaskCommentResponse = JSON.unmarshal(str(resp.content, UTF_8), ListTaskCommentResponse)
        response.raw = resp

        return response

    def update(self, request: UpdateTaskCommentRequest,
               option: Optional[RequestOption] = None) -> UpdateTaskCommentResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateTaskCommentResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateTaskCommentResponse)
        response.raw = resp

        return response
