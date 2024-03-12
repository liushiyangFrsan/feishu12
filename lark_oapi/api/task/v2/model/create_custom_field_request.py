# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .input_custom_field import InputCustomField


class CreateCustomFieldRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[InputCustomField] = None

    @staticmethod
    def builder() -> "CreateCustomFieldRequestBuilder":
        return CreateCustomFieldRequestBuilder()


class CreateCustomFieldRequestBuilder(object):

    def __init__(self) -> None:
        create_custom_field_request = CreateCustomFieldRequest()
        create_custom_field_request.http_method = HttpMethod.POST
        create_custom_field_request.uri = "/open-apis/task/v2/custom_fields"
        create_custom_field_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_custom_field_request: CreateCustomFieldRequest = create_custom_field_request

    def user_id_type(self, user_id_type: str) -> "CreateCustomFieldRequestBuilder":
        self._create_custom_field_request.user_id_type = user_id_type
        self._create_custom_field_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: InputCustomField) -> "CreateCustomFieldRequestBuilder":
        self._create_custom_field_request.request_body = request_body
        self._create_custom_field_request.body = request_body
        return self

    def build(self) -> CreateCustomFieldRequest:
        return self._create_custom_field_request