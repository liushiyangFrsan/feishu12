# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .copy_file_request_body import CopyFileRequestBody


class CopyFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file_token: Optional[str] = None
        self.request_body: Optional[CopyFileRequestBody] = None

    @staticmethod
    def builder() -> "CopyFileRequestBuilder":
        return CopyFileRequestBuilder()


class CopyFileRequestBuilder(object):

    def __init__(self, copy_file_request: CopyFileRequest = CopyFileRequest()) -> None:
        copy_file_request.http_method = HttpMethod.POST
        copy_file_request.uri = "/open-apis/drive/v1/files/:file_token/copy"
        copy_file_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._copy_file_request: CopyFileRequest = copy_file_request

    def file_token(self, file_token: str) -> "CopyFileRequestBuilder":
        self._copy_file_request.file_token = file_token
        self._copy_file_request.paths["file_token"] = str(file_token)
        return self

    def request_body(self, request_body: CopyFileRequestBody) -> "CopyFileRequestBuilder":
        self._copy_file_request.request_body = request_body
        self._copy_file_request.body = request_body
        return self

    def build(self) -> CopyFileRequest:
        return self._copy_file_request
