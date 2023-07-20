# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListAppDashboardRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.app_token: Optional[str] = None

    @staticmethod
    def builder() -> "ListAppDashboardRequestBuilder":
        return ListAppDashboardRequestBuilder()


class ListAppDashboardRequestBuilder(object):

    def __init__(self, list_app_dashboard_request: ListAppDashboardRequest = ListAppDashboardRequest()) -> None:
        list_app_dashboard_request.http_method = HttpMethod.GET
        list_app_dashboard_request.uri = "/open-apis/bitable/v1/apps/:app_token/dashboards"
        list_app_dashboard_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_app_dashboard_request: ListAppDashboardRequest = list_app_dashboard_request

    def page_size(self, page_size: int) -> "ListAppDashboardRequestBuilder":
        self._list_app_dashboard_request.page_size = page_size
        self._list_app_dashboard_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListAppDashboardRequestBuilder":
        self._list_app_dashboard_request.page_token = page_token
        self._list_app_dashboard_request.add_query("page_token", page_token)
        return self

    def app_token(self, app_token: str) -> "ListAppDashboardRequestBuilder":
        self._list_app_dashboard_request.app_token = app_token
        self._list_app_dashboard_request.paths["app_token"] = str(app_token)
        return self

    def build(self) -> ListAppDashboardRequest:
        return self._list_app_dashboard_request
