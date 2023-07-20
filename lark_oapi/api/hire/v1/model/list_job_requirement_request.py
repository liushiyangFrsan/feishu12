# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListJobRequirementRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.job_id: Optional[str] = None
        self.create_time_begin: Optional[str] = None
        self.create_time_end: Optional[str] = None
        self.update_time_begin: Optional[str] = None
        self.update_time_end: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "ListJobRequirementRequestBuilder":
        return ListJobRequirementRequestBuilder()


class ListJobRequirementRequestBuilder(object):

    def __init__(self, list_job_requirement_request: ListJobRequirementRequest = ListJobRequirementRequest()) -> None:
        list_job_requirement_request.http_method = HttpMethod.GET
        list_job_requirement_request.uri = "/open-apis/hire/v1/job_requirements"
        list_job_requirement_request.token_types = {AccessTokenType.TENANT}
        self._list_job_requirement_request: ListJobRequirementRequest = list_job_requirement_request

    def page_token(self, page_token: str) -> "ListJobRequirementRequestBuilder":
        self._list_job_requirement_request.page_token = page_token
        self._list_job_requirement_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListJobRequirementRequestBuilder":
        self._list_job_requirement_request.page_size = page_size
        self._list_job_requirement_request.add_query("page_size", page_size)
        return self

    def job_id(self, job_id: str) -> "ListJobRequirementRequestBuilder":
        self._list_job_requirement_request.job_id = job_id
        self._list_job_requirement_request.add_query("job_id", job_id)
        return self

    def create_time_begin(self, create_time_begin: str) -> "ListJobRequirementRequestBuilder":
        self._list_job_requirement_request.create_time_begin = create_time_begin
        self._list_job_requirement_request.add_query("create_time_begin", create_time_begin)
        return self

    def create_time_end(self, create_time_end: str) -> "ListJobRequirementRequestBuilder":
        self._list_job_requirement_request.create_time_end = create_time_end
        self._list_job_requirement_request.add_query("create_time_end", create_time_end)
        return self

    def update_time_begin(self, update_time_begin: str) -> "ListJobRequirementRequestBuilder":
        self._list_job_requirement_request.update_time_begin = update_time_begin
        self._list_job_requirement_request.add_query("update_time_begin", update_time_begin)
        return self

    def update_time_end(self, update_time_end: str) -> "ListJobRequirementRequestBuilder":
        self._list_job_requirement_request.update_time_end = update_time_end
        self._list_job_requirement_request.add_query("update_time_end", update_time_end)
        return self

    def user_id_type(self, user_id_type: str) -> "ListJobRequirementRequestBuilder":
        self._list_job_requirement_request.user_id_type = user_id_type
        self._list_job_requirement_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "ListJobRequirementRequestBuilder":
        self._list_job_requirement_request.department_id_type = department_id_type
        self._list_job_requirement_request.add_query("department_id_type", department_id_type)
        return self

    def build(self) -> ListJobRequirementRequest:
        return self._list_job_requirement_request
