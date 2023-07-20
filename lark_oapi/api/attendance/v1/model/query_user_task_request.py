# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .query_user_task_request_body import QueryUserTaskRequestBody


class QueryUserTaskRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.employee_type: Optional[str] = None
        self.ignore_invalid_users: Optional[bool] = None
        self.include_terminated_user: Optional[bool] = None
        self.request_body: Optional[QueryUserTaskRequestBody] = None

    @staticmethod
    def builder() -> "QueryUserTaskRequestBuilder":
        return QueryUserTaskRequestBuilder()


class QueryUserTaskRequestBuilder(object):

    def __init__(self, query_user_task_request: QueryUserTaskRequest = QueryUserTaskRequest()) -> None:
        query_user_task_request.http_method = HttpMethod.POST
        query_user_task_request.uri = "/open-apis/attendance/v1/user_tasks/query"
        query_user_task_request.token_types = {AccessTokenType.TENANT}
        self._query_user_task_request: QueryUserTaskRequest = query_user_task_request

    def employee_type(self, employee_type: str) -> "QueryUserTaskRequestBuilder":
        self._query_user_task_request.employee_type = employee_type
        self._query_user_task_request.add_query("employee_type", employee_type)
        return self

    def ignore_invalid_users(self, ignore_invalid_users: bool) -> "QueryUserTaskRequestBuilder":
        self._query_user_task_request.ignore_invalid_users = ignore_invalid_users
        self._query_user_task_request.add_query("ignore_invalid_users", ignore_invalid_users)
        return self

    def include_terminated_user(self, include_terminated_user: bool) -> "QueryUserTaskRequestBuilder":
        self._query_user_task_request.include_terminated_user = include_terminated_user
        self._query_user_task_request.add_query("include_terminated_user", include_terminated_user)
        return self

    def request_body(self, request_body: QueryUserTaskRequestBody) -> "QueryUserTaskRequestBuilder":
        self._query_user_task_request.request_body = request_body
        self._query_user_task_request.body = request_body
        return self

    def build(self) -> QueryUserTaskRequest:
        return self._query_user_task_request
