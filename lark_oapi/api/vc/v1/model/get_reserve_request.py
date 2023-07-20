# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetReserveRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.reserve_id: Optional[int] = None

    @staticmethod
    def builder() -> "GetReserveRequestBuilder":
        return GetReserveRequestBuilder()


class GetReserveRequestBuilder(object):

    def __init__(self, get_reserve_request: GetReserveRequest = GetReserveRequest()) -> None:
        get_reserve_request.http_method = HttpMethod.GET
        get_reserve_request.uri = "/open-apis/vc/v1/reserves/:reserve_id"
        get_reserve_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._get_reserve_request: GetReserveRequest = get_reserve_request

    def user_id_type(self, user_id_type: str) -> "GetReserveRequestBuilder":
        self._get_reserve_request.user_id_type = user_id_type
        self._get_reserve_request.add_query("user_id_type", user_id_type)
        return self

    def reserve_id(self, reserve_id: int) -> "GetReserveRequestBuilder":
        self._get_reserve_request.reserve_id = reserve_id
        self._get_reserve_request.paths["reserve_id"] = str(reserve_id)
        return self

    def build(self) -> GetReserveRequest:
        return self._get_reserve_request
