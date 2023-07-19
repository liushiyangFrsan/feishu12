# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .category import Category


class ListCategoryResponseBody(object):
    _types = {
        "categories": List[Category],
    }

    def __init__(self, d):
        self.categories: Optional[List[Category]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListCategoryResponseBodyBuilder":
        return ListCategoryResponseBodyBuilder()


class ListCategoryResponseBodyBuilder(object):
    def __init__(self, list_category_response_body: ListCategoryResponseBody = ListCategoryResponseBody({})) -> None:
        self._list_category_response_body: ListCategoryResponseBody = list_category_response_body

    def categories(self, categories: List[Category]) -> "ListCategoryResponseBodyBuilder":
        self._list_category_response_body.categories = categories
        return self

    def build(self) -> "ListCategoryResponseBody":
        return self._list_category_response_body