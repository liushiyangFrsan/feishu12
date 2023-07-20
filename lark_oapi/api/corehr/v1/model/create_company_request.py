# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .company import Company


class CreateCompanyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.request_body: Optional[Company] = None

    @staticmethod
    def builder() -> "CreateCompanyRequestBuilder":
        return CreateCompanyRequestBuilder()


class CreateCompanyRequestBuilder(object):

    def __init__(self, create_company_request: CreateCompanyRequest = CreateCompanyRequest()) -> None:
        create_company_request.http_method = HttpMethod.POST
        create_company_request.uri = "/open-apis/corehr/v1/companies"
        create_company_request.token_types = {AccessTokenType.TENANT}
        self._create_company_request: CreateCompanyRequest = create_company_request

    def client_token(self, client_token: str) -> "CreateCompanyRequestBuilder":
        self._create_company_request.client_token = client_token
        self._create_company_request.add_query("client_token", client_token)
        return self

    def request_body(self, request_body: Company) -> "CreateCompanyRequestBuilder":
        self._create_company_request.request_body = request_body
        self._create_company_request.body = request_body
        return self

    def build(self) -> CreateCompanyRequest:
        return self._create_company_request
