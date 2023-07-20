# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .task_search import TaskSearch


class SearchTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[TaskSearch] = None

    @staticmethod
    def builder() -> "SearchTaskRequestBuilder":
        return SearchTaskRequestBuilder()


class SearchTaskRequestBuilder(object):

    def __init__(self, search_task_request: SearchTaskRequest = SearchTaskRequest()) -> None:
        search_task_request.http_method = HttpMethod.POST
        search_task_request.uri = "/open-apis/approval/v4/tasks/search"
        search_task_request.token_types = {AccessTokenType.TENANT}
        self._search_task_request: SearchTaskRequest = search_task_request

    def page_size(self, page_size: int) -> "SearchTaskRequestBuilder":
        self._search_task_request.page_size = page_size
        self._search_task_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "SearchTaskRequestBuilder":
        self._search_task_request.page_token = page_token
        self._search_task_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "SearchTaskRequestBuilder":
        self._search_task_request.user_id_type = user_id_type
        self._search_task_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: TaskSearch) -> "SearchTaskRequestBuilder":
        self._search_task_request.request_body = request_body
        self._search_task_request.body = request_body
        return self

    def build(self) -> SearchTaskRequest:
        return self._search_task_request
