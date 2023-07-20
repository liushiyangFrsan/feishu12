# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .create_identity_request_body import CreateIdentityRequestBody


class CreateIdentityRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[CreateIdentityRequestBody] = None

    @staticmethod
    def builder() -> "CreateIdentityRequestBuilder":
        return CreateIdentityRequestBuilder()


class CreateIdentityRequestBuilder(object):

    def __init__(self, create_identity_request: CreateIdentityRequest = CreateIdentityRequest()) -> None:
        create_identity_request.http_method = HttpMethod.POST
        create_identity_request.uri = "/open-apis/human_authentication/v1/identities"
        create_identity_request.token_types = {AccessTokenType.TENANT}
        self._create_identity_request: CreateIdentityRequest = create_identity_request
    
    def user_id(self, user_id: str) -> "CreateIdentityRequestBuilder":
        self._create_identity_request.user_id = user_id
        self._create_identity_request.add_query("user_id", user_id)
        return self
    
    def user_id_type(self, user_id_type: str) -> "CreateIdentityRequestBuilder":
        self._create_identity_request.user_id_type = user_id_type
        self._create_identity_request.add_query("user_id_type", user_id_type)
        return self
    
    def request_body(self, request_body: CreateIdentityRequestBody) -> "CreateIdentityRequestBuilder":
        self._create_identity_request.request_body = request_body
        self._create_identity_request.body = request_body
        return self

    def build(self) -> CreateIdentityRequest:
        return self._create_identity_request
