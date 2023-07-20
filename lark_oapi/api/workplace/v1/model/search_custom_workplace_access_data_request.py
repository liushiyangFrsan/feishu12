# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class SearchCustomWorkplaceAccessDataRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.from_date: Optional[str] = None
        self.to_date: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.custom_workplace_id: Optional[str] = None

    @staticmethod
    def builder() -> "SearchCustomWorkplaceAccessDataRequestBuilder":
        return SearchCustomWorkplaceAccessDataRequestBuilder()


class SearchCustomWorkplaceAccessDataRequestBuilder(object):

    def __init__(self,
                 search_custom_workplace_access_data_request: SearchCustomWorkplaceAccessDataRequest = SearchCustomWorkplaceAccessDataRequest()) -> None:
        search_custom_workplace_access_data_request.http_method = HttpMethod.POST
        search_custom_workplace_access_data_request.uri = "/open-apis/workplace/v1/custom_workplace_access_data/search"
        search_custom_workplace_access_data_request.token_types = {AccessTokenType.TENANT}
        self._search_custom_workplace_access_data_request: SearchCustomWorkplaceAccessDataRequest = search_custom_workplace_access_data_request

    def from_date(self, from_date: str) -> "SearchCustomWorkplaceAccessDataRequestBuilder":
        self._search_custom_workplace_access_data_request.from_date = from_date
        self._search_custom_workplace_access_data_request.add_query("from_date", from_date)
        return self

    def to_date(self, to_date: str) -> "SearchCustomWorkplaceAccessDataRequestBuilder":
        self._search_custom_workplace_access_data_request.to_date = to_date
        self._search_custom_workplace_access_data_request.add_query("to_date", to_date)
        return self

    def page_size(self, page_size: int) -> "SearchCustomWorkplaceAccessDataRequestBuilder":
        self._search_custom_workplace_access_data_request.page_size = page_size
        self._search_custom_workplace_access_data_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "SearchCustomWorkplaceAccessDataRequestBuilder":
        self._search_custom_workplace_access_data_request.page_token = page_token
        self._search_custom_workplace_access_data_request.add_query("page_token", page_token)
        return self

    def custom_workplace_id(self, custom_workplace_id: str) -> "SearchCustomWorkplaceAccessDataRequestBuilder":
        self._search_custom_workplace_access_data_request.custom_workplace_id = custom_workplace_id
        self._search_custom_workplace_access_data_request.add_query("custom_workplace_id", custom_workplace_id)
        return self

    def build(self) -> SearchCustomWorkplaceAccessDataRequest:
        return self._search_custom_workplace_access_data_request
