# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .patch_reserve_config_request_body import PatchReserveConfigRequestBody


class PatchReserveConfigRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.reserve_config_id: Optional[str] = None
        self.request_body: Optional[PatchReserveConfigRequestBody] = None

    @staticmethod
    def builder() -> "PatchReserveConfigRequestBuilder":
        return PatchReserveConfigRequestBuilder()


class PatchReserveConfigRequestBuilder(object):

    def __init__(self, patch_reserve_config_request: PatchReserveConfigRequest = PatchReserveConfigRequest()) -> None:
        patch_reserve_config_request.http_method = HttpMethod.PATCH
        patch_reserve_config_request.uri = "/open-apis/vc/v1/reserve_configs/:reserve_config_id"
        patch_reserve_config_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._patch_reserve_config_request: PatchReserveConfigRequest = patch_reserve_config_request

    def user_id_type(self, user_id_type: str) -> "PatchReserveConfigRequestBuilder":
        self._patch_reserve_config_request.user_id_type = user_id_type
        self._patch_reserve_config_request.add_query("user_id_type", user_id_type)
        return self

    def reserve_config_id(self, reserve_config_id: str) -> "PatchReserveConfigRequestBuilder":
        self._patch_reserve_config_request.reserve_config_id = reserve_config_id
        self._patch_reserve_config_request.paths["reserve_config_id"] = str(reserve_config_id)
        return self

    def request_body(self, request_body: PatchReserveConfigRequestBody) -> "PatchReserveConfigRequestBuilder":
        self._patch_reserve_config_request.request_body = request_body
        self._patch_reserve_config_request.body = request_body
        return self

    def build(self) -> PatchReserveConfigRequest:
        return self._patch_reserve_config_request
