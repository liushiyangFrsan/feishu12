# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteCategoryRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteCategoryRequestBuilder":
        return DeleteCategoryRequestBuilder()


class DeleteCategoryRequestBuilder(object):

    def __init__(self, delete_category_request: DeleteCategoryRequest = DeleteCategoryRequest()) -> None:
        delete_category_request.http_method = HttpMethod.DELETE
        delete_category_request.uri = "/open-apis/helpdesk/v1/categories/:id"
        delete_category_request.token_types = {AccessTokenType.USER}
        self._delete_category_request: DeleteCategoryRequest = delete_category_request

    def id(self, id: str) -> "DeleteCategoryRequestBuilder":
        self._delete_category_request.id = id
        self._delete_category_request.paths["id"] = id
        return self

    def build(self) -> DeleteCategoryRequest:
        return self._delete_category_request