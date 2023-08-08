# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.delete_batch_message_request import DeleteBatchMessageRequest
from ..model.delete_batch_message_response import DeleteBatchMessageResponse
from ..model.get_progress_batch_message_request import GetProgressBatchMessageRequest
from ..model.get_progress_batch_message_response import GetProgressBatchMessageResponse
from ..model.read_user_batch_message_request import ReadUserBatchMessageRequest
from ..model.read_user_batch_message_response import ReadUserBatchMessageResponse


class BatchMessage(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def delete(self, request: DeleteBatchMessageRequest,
               option: Optional[RequestOption] = None) -> DeleteBatchMessageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteBatchMessageResponse = JSON.unmarshal(str(resp.content, UTF_8), DeleteBatchMessageResponse)
        response.raw = resp

        return response

    def get_progress(self, request: GetProgressBatchMessageRequest,
                     option: Optional[RequestOption] = None) -> GetProgressBatchMessageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetProgressBatchMessageResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   GetProgressBatchMessageResponse)
        response.raw = resp

        return response

    def read_user(self, request: ReadUserBatchMessageRequest,
                  option: Optional[RequestOption] = None) -> ReadUserBatchMessageResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ReadUserBatchMessageResponse = JSON.unmarshal(str(resp.content, UTF_8), ReadUserBatchMessageResponse)
        response.raw = resp

        return response
