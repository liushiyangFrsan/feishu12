# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListPeriodRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None

    @staticmethod
    def builder() -> "ListPeriodRequestBuilder":
        return ListPeriodRequestBuilder()


class ListPeriodRequestBuilder(object):

    def __init__(self, list_period_request: ListPeriodRequest = ListPeriodRequest()) -> None:
        list_period_request.http_method = HttpMethod.GET
        list_period_request.uri = "/open-apis/okr/v1/periods"
        list_period_request.token_types = {AccessTokenType.TENANT}
        self._list_period_request: ListPeriodRequest = list_period_request

    def page_token(self, page_token: str) -> "ListPeriodRequestBuilder":
        self._list_period_request.page_token = page_token
        self._list_period_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListPeriodRequestBuilder":
        self._list_period_request.page_size = page_size
        self._list_period_request.add_query("page_size", page_size)
        return self

    def build(self) -> ListPeriodRequest:
        return self._list_period_request
