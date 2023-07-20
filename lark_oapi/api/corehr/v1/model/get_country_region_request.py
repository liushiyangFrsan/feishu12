# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetCountryRegionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.country_region_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetCountryRegionRequestBuilder":
        return GetCountryRegionRequestBuilder()


class GetCountryRegionRequestBuilder(object):

    def __init__(self, get_country_region_request: GetCountryRegionRequest = GetCountryRegionRequest()) -> None:
        get_country_region_request.http_method = HttpMethod.GET
        get_country_region_request.uri = "/open-apis/corehr/v1/country_regions/:country_region_id"
        get_country_region_request.token_types = {AccessTokenType.TENANT}
        self._get_country_region_request: GetCountryRegionRequest = get_country_region_request

    def country_region_id(self, country_region_id: str) -> "GetCountryRegionRequestBuilder":
        self._get_country_region_request.country_region_id = country_region_id
        self._get_country_region_request.paths["country_region_id"] = str(country_region_id)
        return self

    def build(self) -> GetCountryRegionRequest:
        return self._get_country_region_request
