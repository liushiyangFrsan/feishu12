# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.api.mail.v1.model.batch_create_mailgroup_member_request import BatchCreateMailgroupMemberRequest
from lark_oapi.api.mail.v1.model.batch_create_mailgroup_member_response import BatchCreateMailgroupMemberResponse
from lark_oapi.api.mail.v1.model.batch_delete_mailgroup_member_request import BatchDeleteMailgroupMemberRequest
from lark_oapi.api.mail.v1.model.batch_delete_mailgroup_member_response import BatchDeleteMailgroupMemberResponse
from lark_oapi.api.mail.v1.model.create_mailgroup_member_request import CreateMailgroupMemberRequest
from lark_oapi.api.mail.v1.model.create_mailgroup_member_response import CreateMailgroupMemberResponse
from lark_oapi.api.mail.v1.model.delete_mailgroup_member_request import DeleteMailgroupMemberRequest
from lark_oapi.api.mail.v1.model.delete_mailgroup_member_response import DeleteMailgroupMemberResponse
from lark_oapi.api.mail.v1.model.get_mailgroup_member_request import GetMailgroupMemberRequest
from lark_oapi.api.mail.v1.model.get_mailgroup_member_response import GetMailgroupMemberResponse
from lark_oapi.api.mail.v1.model.list_mailgroup_member_request import ListMailgroupMemberRequest
from lark_oapi.api.mail.v1.model.list_mailgroup_member_response import ListMailgroupMemberResponse
from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify


class MailgroupMember(object):
    def __init__(self, config: Config) -> None:
        self.config: Optional[Config] = config

    def batch_create(self, request: BatchCreateMailgroupMemberRequest,
                     option: RequestOption = RequestOption()) -> BatchCreateMailgroupMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchCreateMailgroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                      BatchCreateMailgroupMemberResponse)
        response.raw = resp

        return response

    def batch_delete(self, request: BatchDeleteMailgroupMemberRequest,
                     option: RequestOption = RequestOption()) -> BatchDeleteMailgroupMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: BatchDeleteMailgroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                      BatchDeleteMailgroupMemberResponse)
        response.raw = resp

        return response

    def create(self, request: CreateMailgroupMemberRequest,
               option: RequestOption = RequestOption()) -> CreateMailgroupMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateMailgroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 CreateMailgroupMemberResponse)
        response.raw = resp

        return response

    def delete(self, request: DeleteMailgroupMemberRequest,
               option: RequestOption = RequestOption()) -> DeleteMailgroupMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: DeleteMailgroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 DeleteMailgroupMemberResponse)
        response.raw = resp

        return response

    def get(self, request: GetMailgroupMemberRequest,
            option: RequestOption = RequestOption()) -> GetMailgroupMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetMailgroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), GetMailgroupMemberResponse)
        response.raw = resp

        return response

    def list(self, request: ListMailgroupMemberRequest,
             option: RequestOption = RequestOption()) -> ListMailgroupMemberResponse:
        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListMailgroupMemberResponse = JSON.unmarshal(str(resp.content, UTF_8), ListMailgroupMemberResponse)
        response.raw = resp

        return response