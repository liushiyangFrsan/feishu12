# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_delete_mailgroup_member_request_body import BatchDeleteMailgroupMemberRequestBody


class BatchDeleteMailgroupMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.mailgroup_id: Optional[str] = None
        self.request_body: Optional[BatchDeleteMailgroupMemberRequestBody] = None

    @staticmethod
    def builder() -> "BatchDeleteMailgroupMemberRequestBuilder":
        return BatchDeleteMailgroupMemberRequestBuilder()


class BatchDeleteMailgroupMemberRequestBuilder(object):

    def __init__(self,
                 batch_delete_mailgroup_member_request: BatchDeleteMailgroupMemberRequest = BatchDeleteMailgroupMemberRequest()) -> None:
        batch_delete_mailgroup_member_request.http_method = HttpMethod.DELETE
        batch_delete_mailgroup_member_request.uri = "/open-apis/mail/v1/mailgroups/:mailgroup_id/members/batch_delete"
        batch_delete_mailgroup_member_request.token_types = {AccessTokenType.TENANT}
        self._batch_delete_mailgroup_member_request: BatchDeleteMailgroupMemberRequest = batch_delete_mailgroup_member_request

    def mailgroup_id(self, mailgroup_id: str) -> "BatchDeleteMailgroupMemberRequestBuilder":
        self._batch_delete_mailgroup_member_request.mailgroup_id = mailgroup_id
        self._batch_delete_mailgroup_member_request.paths["mailgroup_id"] = str(mailgroup_id)
        return self

    def request_body(self,
                     request_body: BatchDeleteMailgroupMemberRequestBody) -> "BatchDeleteMailgroupMemberRequestBuilder":
        self._batch_delete_mailgroup_member_request.request_body = request_body
        self._batch_delete_mailgroup_member_request.body = request_body
        return self

    def build(self) -> BatchDeleteMailgroupMemberRequest:
        return self._batch_delete_mailgroup_member_request
