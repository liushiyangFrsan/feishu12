# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListSubregionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None
        self.subdivision_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListSubregionRequestBuilder":
        return ListSubregionRequestBuilder()


class ListSubregionRequestBuilder(object):

    def __init__(self, list_subregion_request: ListSubregionRequest = ListSubregionRequest()) -> None:
        list_subregion_request.http_method = HttpMethod.GET
        list_subregion_request.uri = "/open-apis/corehr/v1/subregions"
        list_subregion_request.token_types = {AccessTokenType.TENANT}
        self._list_subregion_request: ListSubregionRequest = list_subregion_request

    def page_token(self, page_token: str) -> "ListSubregionRequestBuilder":
        self._list_subregion_request.page_token = page_token
        self._list_subregion_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: str) -> "ListSubregionRequestBuilder":
        self._list_subregion_request.page_size = page_size
        self._list_subregion_request.add_query("page_size", page_size)
        return self

    def subdivision_id(self, subdivision_id: str) -> "ListSubregionRequestBuilder":
        self._list_subregion_request.subdivision_id = subdivision_id
        self._list_subregion_request.add_query("subdivision_id", subdivision_id)
        return self

    def build(self) -> ListSubregionRequest:
        return self._list_subregion_request
