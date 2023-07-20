# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .base_member import BaseMember


class CreatePermissionMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.type: Optional[str] = None
        self.need_notification: Optional[bool] = None
        self.token: Optional[str] = None
        self.request_body: Optional[BaseMember] = None

    @staticmethod
    def builder() -> "CreatePermissionMemberRequestBuilder":
        return CreatePermissionMemberRequestBuilder()


class CreatePermissionMemberRequestBuilder(object):

    def __init__(self,
                 create_permission_member_request: CreatePermissionMemberRequest = CreatePermissionMemberRequest()) -> None:
        create_permission_member_request.http_method = HttpMethod.POST
        create_permission_member_request.uri = "/open-apis/drive/v1/permissions/:token/members"
        create_permission_member_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_permission_member_request: CreatePermissionMemberRequest = create_permission_member_request

    def type(self, type: str) -> "CreatePermissionMemberRequestBuilder":
        self._create_permission_member_request.type = type
        self._create_permission_member_request.add_query("type", type)
        return self

    def need_notification(self, need_notification: bool) -> "CreatePermissionMemberRequestBuilder":
        self._create_permission_member_request.need_notification = need_notification
        self._create_permission_member_request.add_query("need_notification", need_notification)
        return self

    def token(self, token: str) -> "CreatePermissionMemberRequestBuilder":
        self._create_permission_member_request.token = token
        self._create_permission_member_request.paths["token"] = str(token)
        return self

    def request_body(self, request_body: BaseMember) -> "CreatePermissionMemberRequestBuilder":
        self._create_permission_member_request.request_body = request_body
        self._create_permission_member_request.body = request_body
        return self

    def build(self) -> CreatePermissionMemberRequest:
        return self._create_permission_member_request
