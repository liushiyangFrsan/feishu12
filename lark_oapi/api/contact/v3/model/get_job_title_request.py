# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetJobTitleRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.job_title_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetJobTitleRequestBuilder":
        return GetJobTitleRequestBuilder()


class GetJobTitleRequestBuilder(object):

    def __init__(self, get_job_title_request: GetJobTitleRequest = GetJobTitleRequest()) -> None:
        get_job_title_request.http_method = HttpMethod.GET
        get_job_title_request.uri = "/open-apis/contact/v3/job_titles/:job_title_id"
        get_job_title_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_job_title_request: GetJobTitleRequest = get_job_title_request

    def job_title_id(self, job_title_id: str) -> "GetJobTitleRequestBuilder":
        self._get_job_title_request.job_title_id = job_title_id
        self._get_job_title_request.paths["job_title_id"] = str(job_title_id)
        return self

    def build(self) -> GetJobTitleRequest:
        return self._get_job_title_request
