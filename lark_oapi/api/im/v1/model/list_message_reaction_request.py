# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListMessageReactionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.reaction_type: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.user_id_type: Optional[str] = None
        self.message_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListMessageReactionRequestBuilder":
        return ListMessageReactionRequestBuilder()


class ListMessageReactionRequestBuilder(object):

    def __init__(self,
                 list_message_reaction_request: ListMessageReactionRequest = ListMessageReactionRequest()) -> None:
        list_message_reaction_request.http_method = HttpMethod.GET
        list_message_reaction_request.uri = "/open-apis/im/v1/messages/:message_id/reactions"
        list_message_reaction_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._list_message_reaction_request: ListMessageReactionRequest = list_message_reaction_request

    def reaction_type(self, reaction_type: str) -> "ListMessageReactionRequestBuilder":
        self._list_message_reaction_request.reaction_type = reaction_type
        self._list_message_reaction_request.add_query("reaction_type", reaction_type)
        return self

    def page_token(self, page_token: str) -> "ListMessageReactionRequestBuilder":
        self._list_message_reaction_request.page_token = page_token
        self._list_message_reaction_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListMessageReactionRequestBuilder":
        self._list_message_reaction_request.page_size = page_size
        self._list_message_reaction_request.add_query("page_size", page_size)
        return self

    def user_id_type(self, user_id_type: str) -> "ListMessageReactionRequestBuilder":
        self._list_message_reaction_request.user_id_type = user_id_type
        self._list_message_reaction_request.add_query("user_id_type", user_id_type)
        return self

    def message_id(self, message_id: str) -> "ListMessageReactionRequestBuilder":
        self._list_message_reaction_request.message_id = message_id
        self._list_message_reaction_request.paths["message_id"] = str(message_id)
        return self

    def build(self) -> ListMessageReactionRequest:
        return self._list_message_reaction_request
