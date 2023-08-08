# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.approve_task_request import ApproveTaskRequest
from ..model.approve_task_response import ApproveTaskResponse
from ..model.query_task_request import QueryTaskRequest
from ..model.query_task_response import QueryTaskResponse
from ..model.reject_task_request import RejectTaskRequest
from ..model.reject_task_response import RejectTaskResponse
from ..model.resubmit_task_request import ResubmitTaskRequest
from ..model.resubmit_task_response import ResubmitTaskResponse
from ..model.search_task_request import SearchTaskRequest
from ..model.search_task_response import SearchTaskResponse
from ..model.transfer_task_request import TransferTaskRequest
from ..model.transfer_task_response import TransferTaskResponse


class Task(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def approve(self, request: ApproveTaskRequest, option: Optional[RequestOption] = None) -> ApproveTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ApproveTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), ApproveTaskResponse)
        response.raw = resp

        return response

    def query(self, request: QueryTaskRequest, option: Optional[RequestOption] = None) -> QueryTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QueryTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), QueryTaskResponse)
        response.raw = resp

        return response

    def reject(self, request: RejectTaskRequest, option: Optional[RequestOption] = None) -> RejectTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: RejectTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), RejectTaskResponse)
        response.raw = resp

        return response

    def resubmit(self, request: ResubmitTaskRequest, option: Optional[RequestOption] = None) -> ResubmitTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ResubmitTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), ResubmitTaskResponse)
        response.raw = resp

        return response

    def search(self, request: SearchTaskRequest, option: Optional[RequestOption] = None) -> SearchTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: SearchTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), SearchTaskResponse)
        response.raw = resp

        return response

    def transfer(self, request: TransferTaskRequest, option: Optional[RequestOption] = None) -> TransferTaskResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: TransferTaskResponse = JSON.unmarshal(str(resp.content, UTF_8), TransferTaskResponse)
        response.raw = resp

        return response
