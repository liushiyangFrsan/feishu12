# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_delete_functional_role_member_request_body import BatchDeleteFunctionalRoleMemberRequestBody


class BatchDeleteFunctionalRoleMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.role_id: Optional[str] = None
        self.request_body: Optional[BatchDeleteFunctionalRoleMemberRequestBody] = None

    @staticmethod
    def builder() -> "BatchDeleteFunctionalRoleMemberRequestBuilder":
        return BatchDeleteFunctionalRoleMemberRequestBuilder()


class BatchDeleteFunctionalRoleMemberRequestBuilder(object):

    def __init__(self,
                 batch_delete_functional_role_member_request: BatchDeleteFunctionalRoleMemberRequest = BatchDeleteFunctionalRoleMemberRequest()) -> None:
        batch_delete_functional_role_member_request.http_method = HttpMethod.PATCH
        batch_delete_functional_role_member_request.uri = "/open-apis/contact/v3/functional_roles/:role_id/members/batch_delete"
        batch_delete_functional_role_member_request.token_types = {AccessTokenType.TENANT}
        self._batch_delete_functional_role_member_request: BatchDeleteFunctionalRoleMemberRequest = batch_delete_functional_role_member_request

    def user_id_type(self, user_id_type: str) -> "BatchDeleteFunctionalRoleMemberRequestBuilder":
        self._batch_delete_functional_role_member_request.user_id_type = user_id_type
        self._batch_delete_functional_role_member_request.add_query("user_id_type", user_id_type)
        return self

    def role_id(self, role_id: str) -> "BatchDeleteFunctionalRoleMemberRequestBuilder":
        self._batch_delete_functional_role_member_request.role_id = role_id
        self._batch_delete_functional_role_member_request.paths["role_id"] = str(role_id)
        return self

    def request_body(self,
                     request_body: BatchDeleteFunctionalRoleMemberRequestBody) -> "BatchDeleteFunctionalRoleMemberRequestBuilder":
        self._batch_delete_functional_role_member_request.request_body = request_body
        self._batch_delete_functional_role_member_request.body = request_body
        return self

    def build(self) -> BatchDeleteFunctionalRoleMemberRequest:
        return self._batch_delete_functional_role_member_request
