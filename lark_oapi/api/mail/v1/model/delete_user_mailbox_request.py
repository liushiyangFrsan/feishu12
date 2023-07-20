# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteUserMailboxRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.transfer_mailbox: Optional[str] = None
        self.user_mailbox_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteUserMailboxRequestBuilder":
        return DeleteUserMailboxRequestBuilder()


class DeleteUserMailboxRequestBuilder(object):

    def __init__(self, delete_user_mailbox_request: DeleteUserMailboxRequest = DeleteUserMailboxRequest()) -> None:
        delete_user_mailbox_request.http_method = HttpMethod.DELETE
        delete_user_mailbox_request.uri = "/open-apis/mail/v1/user_mailboxes/:user_mailbox_id"
        delete_user_mailbox_request.token_types = {AccessTokenType.TENANT}
        self._delete_user_mailbox_request: DeleteUserMailboxRequest = delete_user_mailbox_request

    def transfer_mailbox(self, transfer_mailbox: str) -> "DeleteUserMailboxRequestBuilder":
        self._delete_user_mailbox_request.transfer_mailbox = transfer_mailbox
        self._delete_user_mailbox_request.add_query("transfer_mailbox", transfer_mailbox)
        return self

    def user_mailbox_id(self, user_mailbox_id: str) -> "DeleteUserMailboxRequestBuilder":
        self._delete_user_mailbox_request.user_mailbox_id = user_mailbox_id
        self._delete_user_mailbox_request.paths["user_mailbox_id"] = str(user_mailbox_id)
        return self

    def build(self) -> DeleteUserMailboxRequest:
        return self._delete_user_mailbox_request
