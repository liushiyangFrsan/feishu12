# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .work_city import WorkCity


class ListWorkCityResponseBody(object):
    _types = {
        "items": List[WorkCity],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[WorkCity]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListWorkCityResponseBodyBuilder":
        return ListWorkCityResponseBodyBuilder()


class ListWorkCityResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_work_city_response_body = ListWorkCityResponseBody()

    def items(self, items: List[WorkCity]) -> "ListWorkCityResponseBodyBuilder":
        self._list_work_city_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListWorkCityResponseBodyBuilder":
        self._list_work_city_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListWorkCityResponseBodyBuilder":
        self._list_work_city_response_body.has_more = has_more
        return self

    def build(self) -> "ListWorkCityResponseBody":
        return self._list_work_city_response_body