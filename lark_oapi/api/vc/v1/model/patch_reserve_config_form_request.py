# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .patch_reserve_config_form_request_body import PatchReserveConfigFormRequestBody


class PatchReserveConfigFormRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.reserve_config_id: Optional[str] = None
        self.request_body: Optional[PatchReserveConfigFormRequestBody] = None

    @staticmethod
    def builder() -> "PatchReserveConfigFormRequestBuilder":
        return PatchReserveConfigFormRequestBuilder()


class PatchReserveConfigFormRequestBuilder(object):

    def __init__(self,
                 patch_reserve_config_form_request: PatchReserveConfigFormRequest = PatchReserveConfigFormRequest()) -> None:
        patch_reserve_config_form_request.http_method = HttpMethod.PATCH
        patch_reserve_config_form_request.uri = "/open-apis/vc/v1/reserve_configs/:reserve_config_id/form"
        patch_reserve_config_form_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._patch_reserve_config_form_request: PatchReserveConfigFormRequest = patch_reserve_config_form_request

    def user_id_type(self, user_id_type: str) -> "PatchReserveConfigFormRequestBuilder":
        self._patch_reserve_config_form_request.user_id_type = user_id_type
        self._patch_reserve_config_form_request.add_query("user_id_type", user_id_type)
        return self

    def reserve_config_id(self, reserve_config_id: str) -> "PatchReserveConfigFormRequestBuilder":
        self._patch_reserve_config_form_request.reserve_config_id = reserve_config_id
        self._patch_reserve_config_form_request.paths["reserve_config_id"] = str(reserve_config_id)
        return self

    def request_body(self, request_body: PatchReserveConfigFormRequestBody) -> "PatchReserveConfigFormRequestBuilder":
        self._patch_reserve_config_form_request.request_body = request_body
        self._patch_reserve_config_form_request.body = request_body
        return self

    def build(self) -> PatchReserveConfigFormRequest:
        return self._patch_reserve_config_form_request
