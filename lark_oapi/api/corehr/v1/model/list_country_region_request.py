# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListCountryRegionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None

    @staticmethod
    def builder() -> "ListCountryRegionRequestBuilder":
        return ListCountryRegionRequestBuilder()


class ListCountryRegionRequestBuilder(object):

    def __init__(self, list_country_region_request: ListCountryRegionRequest = ListCountryRegionRequest()) -> None:
        list_country_region_request.http_method = HttpMethod.GET
        list_country_region_request.uri = "/open-apis/corehr/v1/country_regions"
        list_country_region_request.token_types = {AccessTokenType.TENANT}
        self._list_country_region_request: ListCountryRegionRequest = list_country_region_request

    def page_token(self, page_token: str) -> "ListCountryRegionRequestBuilder":
        self._list_country_region_request.page_token = page_token
        self._list_country_region_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: str) -> "ListCountryRegionRequestBuilder":
        self._list_country_region_request.page_size = page_size
        self._list_country_region_request.add_query("page_size", page_size)
        return self

    def build(self) -> ListCountryRegionRequest:
        return self._list_country_region_request
