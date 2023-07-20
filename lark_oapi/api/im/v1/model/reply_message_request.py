# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .reply_message_request_body import ReplyMessageRequestBody


class ReplyMessageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.message_id: Optional[str] = None
        self.request_body: Optional[ReplyMessageRequestBody] = None

    @staticmethod
    def builder() -> "ReplyMessageRequestBuilder":
        return ReplyMessageRequestBuilder()


class ReplyMessageRequestBuilder(object):

    def __init__(self, reply_message_request: ReplyMessageRequest = ReplyMessageRequest()) -> None:
        reply_message_request.http_method = HttpMethod.POST
        reply_message_request.uri = "/open-apis/im/v1/messages/:message_id/reply"
        reply_message_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._reply_message_request: ReplyMessageRequest = reply_message_request

    def message_id(self, message_id: str) -> "ReplyMessageRequestBuilder":
        self._reply_message_request.message_id = message_id
        self._reply_message_request.paths["message_id"] = str(message_id)
        return self

    def request_body(self, request_body: ReplyMessageRequestBody) -> "ReplyMessageRequestBuilder":
        self._reply_message_request.request_body = request_body
        self._reply_message_request.body = request_body
        return self

    def build(self) -> ReplyMessageRequest:
        return self._reply_message_request
