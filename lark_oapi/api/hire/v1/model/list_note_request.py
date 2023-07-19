# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListNoteRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.talent_id: Optional[str] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListNoteRequestBuilder":
        return ListNoteRequestBuilder()


class ListNoteRequestBuilder(object):

    def __init__(self, list_note_request: ListNoteRequest = ListNoteRequest()) -> None:
        list_note_request.http_method = HttpMethod.GET
        list_note_request.uri = "/open-apis/hire/v1/notes"
        list_note_request.token_types = {AccessTokenType.TENANT}
        self._list_note_request: ListNoteRequest = list_note_request

    def page_size(self, page_size: int) -> "ListNoteRequestBuilder":
        self._list_note_request.page_size = page_size
        self._list_note_request.queries["page_size"] = str(page_size)
        return self

    def page_token(self, page_token: str) -> "ListNoteRequestBuilder":
        self._list_note_request.page_token = page_token
        self._list_note_request.queries["page_token"] = str(page_token)
        return self

    def talent_id(self, talent_id: str) -> "ListNoteRequestBuilder":
        self._list_note_request.talent_id = talent_id
        self._list_note_request.queries["talent_id"] = str(talent_id)
        return self

    def user_id_type(self, user_id_type: str) -> "ListNoteRequestBuilder":
        self._list_note_request.user_id_type = user_id_type
        self._list_note_request.queries["user_id_type"] = str(user_id_type)
        return self

    def build(self) -> ListNoteRequest:
        return self._list_note_request