# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class TasksSectionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.completed: Optional[bool] = None
        self.created_from: Optional[int] = None
        self.created_to: Optional[int] = None
        self.user_id_type: Optional[str] = None
        self.section_guid: Optional[str] = None

    @staticmethod
    def builder() -> "TasksSectionRequestBuilder":
        return TasksSectionRequestBuilder()


class TasksSectionRequestBuilder(object):

    def __init__(self) -> None:
        tasks_section_request = TasksSectionRequest()
        tasks_section_request.http_method = HttpMethod.GET
        tasks_section_request.uri = "/open-apis/task/v2/sections/:section_guid/tasks"
        tasks_section_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._tasks_section_request: TasksSectionRequest = tasks_section_request

    def page_size(self, page_size: int) -> "TasksSectionRequestBuilder":
        self._tasks_section_request.page_size = page_size
        self._tasks_section_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "TasksSectionRequestBuilder":
        self._tasks_section_request.page_token = page_token
        self._tasks_section_request.add_query("page_token", page_token)
        return self

    def completed(self, completed: bool) -> "TasksSectionRequestBuilder":
        self._tasks_section_request.completed = completed
        self._tasks_section_request.add_query("completed", completed)
        return self

    def created_from(self, created_from: int) -> "TasksSectionRequestBuilder":
        self._tasks_section_request.created_from = created_from
        self._tasks_section_request.add_query("created_from", created_from)
        return self

    def created_to(self, created_to: int) -> "TasksSectionRequestBuilder":
        self._tasks_section_request.created_to = created_to
        self._tasks_section_request.add_query("created_to", created_to)
        return self

    def user_id_type(self, user_id_type: str) -> "TasksSectionRequestBuilder":
        self._tasks_section_request.user_id_type = user_id_type
        self._tasks_section_request.add_query("user_id_type", user_id_type)
        return self

    def section_guid(self, section_guid: str) -> "TasksSectionRequestBuilder":
        self._tasks_section_request.section_guid = section_guid
        self._tasks_section_request.paths["section_guid"] = str(section_guid)
        return self

    def build(self) -> TasksSectionRequest:
        return self._tasks_section_request
