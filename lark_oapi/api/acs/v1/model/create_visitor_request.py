# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_visitor_request_body import CreateVisitorRequestBody


class CreateVisitorRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[CreateVisitorRequestBody] = None

    @staticmethod
    def builder() -> "CreateVisitorRequestBuilder":
        return CreateVisitorRequestBuilder()


class CreateVisitorRequestBuilder(object):

    def __init__(self) -> None:
        create_visitor_request = CreateVisitorRequest()
        create_visitor_request.http_method = HttpMethod.POST
        create_visitor_request.uri = "/open-apis/acs/v1/visitors"
        create_visitor_request.token_types = {AccessTokenType.USER}
        self._create_visitor_request: CreateVisitorRequest = create_visitor_request

    def user_id_type(self, user_id_type: str) -> "CreateVisitorRequestBuilder":
        self._create_visitor_request.user_id_type = user_id_type
        self._create_visitor_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: CreateVisitorRequestBody) -> "CreateVisitorRequestBuilder":
        self._create_visitor_request.request_body = request_body
        self._create_visitor_request.body = request_body
        return self

    def build(self) -> CreateVisitorRequest:
        return self._create_visitor_request