# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .location import Location


class CreateLocationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.request_body: Optional[Location] = None

    @staticmethod
    def builder() -> "CreateLocationRequestBuilder":
        return CreateLocationRequestBuilder()


class CreateLocationRequestBuilder(object):

    def __init__(self, create_location_request: CreateLocationRequest = CreateLocationRequest()) -> None:
        create_location_request.http_method = HttpMethod.POST
        create_location_request.uri = "/open-apis/corehr/v1/locations"
        create_location_request.token_types = {AccessTokenType.TENANT}
        self._create_location_request: CreateLocationRequest = create_location_request

    def client_token(self, client_token: str) -> "CreateLocationRequestBuilder":
        self._create_location_request.client_token = client_token
        self._create_location_request.add_query("client_token", client_token)
        return self

    def request_body(self, request_body: Location) -> "CreateLocationRequestBuilder":
        self._create_location_request.request_body = request_body
        self._create_location_request.body = request_body
        return self

    def build(self) -> CreateLocationRequest:
        return self._create_location_request
