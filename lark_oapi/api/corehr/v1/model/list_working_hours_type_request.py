# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListWorkingHoursTypeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[str] = None

    @staticmethod
    def builder() -> "ListWorkingHoursTypeRequestBuilder":
        return ListWorkingHoursTypeRequestBuilder()


class ListWorkingHoursTypeRequestBuilder(object):

    def __init__(self,
                 list_working_hours_type_request: ListWorkingHoursTypeRequest = ListWorkingHoursTypeRequest()) -> None:
        list_working_hours_type_request.http_method = HttpMethod.GET
        list_working_hours_type_request.uri = "/open-apis/corehr/v1/working_hours_types"
        list_working_hours_type_request.token_types = {AccessTokenType.TENANT}
        self._list_working_hours_type_request: ListWorkingHoursTypeRequest = list_working_hours_type_request

    def page_token(self, page_token: str) -> "ListWorkingHoursTypeRequestBuilder":
        self._list_working_hours_type_request.page_token = page_token
        self._list_working_hours_type_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: str) -> "ListWorkingHoursTypeRequestBuilder":
        self._list_working_hours_type_request.page_size = page_size
        self._list_working_hours_type_request.add_query("page_size", page_size)
        return self

    def build(self) -> ListWorkingHoursTypeRequest:
        return self._list_working_hours_type_request
