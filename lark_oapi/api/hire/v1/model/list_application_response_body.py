# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ListApplicationResponseBody(object):
    _types = {
        "items": List[str],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d):
        self.items: Optional[List[str]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListApplicationResponseBodyBuilder":
        return ListApplicationResponseBodyBuilder()


class ListApplicationResponseBodyBuilder(object):
    def __init__(self,
                 list_application_response_body: ListApplicationResponseBody = ListApplicationResponseBody({})) -> None:
        self._list_application_response_body: ListApplicationResponseBody = list_application_response_body

    def items(self, items: List[str]) -> "ListApplicationResponseBodyBuilder":
        self._list_application_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListApplicationResponseBodyBuilder":
        self._list_application_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListApplicationResponseBodyBuilder":
        self._list_application_response_body.has_more = has_more
        return self

    def build(self) -> "ListApplicationResponseBody":
        return self._list_application_response_body