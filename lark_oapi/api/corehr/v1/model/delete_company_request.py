# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteCompanyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.company_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteCompanyRequestBuilder":
        return DeleteCompanyRequestBuilder()


class DeleteCompanyRequestBuilder(object):

    def __init__(self, delete_company_request: DeleteCompanyRequest = DeleteCompanyRequest()) -> None:
        delete_company_request.http_method = HttpMethod.DELETE
        delete_company_request.uri = "/open-apis/corehr/v1/companies/:company_id"
        delete_company_request.token_types = {AccessTokenType.TENANT}
        self._delete_company_request: DeleteCompanyRequest = delete_company_request

    def company_id(self, company_id: str) -> "DeleteCompanyRequestBuilder":
        self._delete_company_request.company_id = company_id
        self._delete_company_request.paths["company_id"] = str(company_id)
        return self

    def build(self) -> DeleteCompanyRequest:
        return self._delete_company_request
