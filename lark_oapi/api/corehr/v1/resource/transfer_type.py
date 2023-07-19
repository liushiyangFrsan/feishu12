# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.corehr.v1.model.query_transfer_type_request import QueryTransferTypeRequest
from lark_oapi.api.corehr.v1.model.query_transfer_type_response import QueryTransferTypeResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class TransferType(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def query(self, request: QueryTransferTypeRequest,
              option: RequestOption = RequestOption()) -> QueryTransferTypeResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: QueryTransferTypeResponse = JSON.unmarshal(str(resp.content, UTF_8), QueryTransferTypeResponse)
        response.raw = resp

        return response