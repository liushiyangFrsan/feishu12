# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .update_progress_record_request_body import UpdateProgressRecordRequestBody


class UpdateProgressRecordRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.progress_id: Optional[int] = None
        self.request_body: Optional[UpdateProgressRecordRequestBody] = None

    @staticmethod
    def builder() -> "UpdateProgressRecordRequestBuilder":
        return UpdateProgressRecordRequestBuilder()


class UpdateProgressRecordRequestBuilder(object):

    def __init__(self,
                 update_progress_record_request: UpdateProgressRecordRequest = UpdateProgressRecordRequest()) -> None:
        update_progress_record_request.http_method = HttpMethod.PUT
        update_progress_record_request.uri = "/open-apis/okr/v1/progress_records/:progress_id"
        update_progress_record_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._update_progress_record_request: UpdateProgressRecordRequest = update_progress_record_request

    def user_id_type(self, user_id_type: str) -> "UpdateProgressRecordRequestBuilder":
        self._update_progress_record_request.user_id_type = user_id_type
        self._update_progress_record_request.add_query("user_id_type", user_id_type)
        return self

    def progress_id(self, progress_id: int) -> "UpdateProgressRecordRequestBuilder":
        self._update_progress_record_request.progress_id = progress_id
        self._update_progress_record_request.paths["progress_id"] = str(progress_id)
        return self

    def request_body(self, request_body: UpdateProgressRecordRequestBody) -> "UpdateProgressRecordRequestBuilder":
        self._update_progress_record_request.request_body = request_body
        self._update_progress_record_request.body = request_body
        return self

    def build(self) -> UpdateProgressRecordRequest:
        return self._update_progress_record_request
