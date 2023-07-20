# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DownloadFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file_id: Optional[str] = None

    @staticmethod
    def builder() -> "DownloadFileRequestBuilder":
        return DownloadFileRequestBuilder()


class DownloadFileRequestBuilder(object):

    def __init__(self, download_file_request: DownloadFileRequest = DownloadFileRequest()) -> None:
        download_file_request.http_method = HttpMethod.GET
        download_file_request.uri = "/open-apis/attendance/v1/files/:file_id/download"
        download_file_request.token_types = {AccessTokenType.TENANT}
        self._download_file_request: DownloadFileRequest = download_file_request

    def file_id(self, file_id: str) -> "DownloadFileRequestBuilder":
        self._download_file_request.file_id = file_id
        self._download_file_request.paths["file_id"] = str(file_id)
        return self

    def build(self) -> DownloadFileRequest:
        return self._download_file_request
