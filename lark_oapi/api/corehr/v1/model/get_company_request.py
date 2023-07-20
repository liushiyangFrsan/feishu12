# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetCompanyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.company_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetCompanyRequestBuilder":
        return GetCompanyRequestBuilder()


class GetCompanyRequestBuilder(object):

    def __init__(self, get_company_request: GetCompanyRequest = GetCompanyRequest()) -> None:
        get_company_request.http_method = HttpMethod.GET
        get_company_request.uri = "/open-apis/corehr/v1/companies/:company_id"
        get_company_request.token_types = {AccessTokenType.TENANT}
        self._get_company_request: GetCompanyRequest = get_company_request

    def company_id(self, company_id: str) -> "GetCompanyRequestBuilder":
        self._get_company_request.company_id = company_id
        self._get_company_request.paths["company_id"] = str(company_id)
        return self

    def build(self) -> GetCompanyRequest:
        return self._get_company_request
