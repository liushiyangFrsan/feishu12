# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.create_ticket_customized_field_request import CreateTicketCustomizedFieldRequest
from ..model.create_ticket_customized_field_response import CreateTicketCustomizedFieldResponse
from ..model.delete_ticket_customized_field_request import DeleteTicketCustomizedFieldRequest
from ..model.delete_ticket_customized_field_response import DeleteTicketCustomizedFieldResponse
from ..model.get_ticket_customized_field_request import GetTicketCustomizedFieldRequest
from ..model.get_ticket_customized_field_response import GetTicketCustomizedFieldResponse
from ..model.list_ticket_customized_field_request import ListTicketCustomizedFieldRequest
from ..model.list_ticket_customized_field_response import ListTicketCustomizedFieldResponse
from ..model.patch_ticket_customized_field_request import PatchTicketCustomizedFieldRequest
from ..model.patch_ticket_customized_field_response import PatchTicketCustomizedFieldResponse


class TicketCustomizedField(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateTicketCustomizedFieldRequest,
               option: Optional[RequestOption] = None) -> CreateTicketCustomizedFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateTicketCustomizedFieldResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                       CreateTicketCustomizedFieldResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteTicketCustomizedFieldRequest,
               option: Optional[RequestOption] = None) -> DeleteTicketCustomizedFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteTicketCustomizedFieldResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                       DeleteTicketCustomizedFieldResponse)
        response.raw = resp

        return response

    def get(self, request: GetTicketCustomizedFieldRequest,
            option: Optional[RequestOption] = None) -> GetTicketCustomizedFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetTicketCustomizedFieldResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                    GetTicketCustomizedFieldResponse)
        response.raw = resp

        return response

    def list(self, request: ListTicketCustomizedFieldRequest,
             option: Optional[RequestOption] = None) -> ListTicketCustomizedFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListTicketCustomizedFieldResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                     ListTicketCustomizedFieldResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchTicketCustomizedFieldRequest,
              option: Optional[RequestOption] = None) -> PatchTicketCustomizedFieldResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: PatchTicketCustomizedFieldResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                      PatchTicketCustomizedFieldResponse)
        response.raw = resp

        return response
