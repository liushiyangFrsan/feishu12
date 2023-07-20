# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListMailgroupManagerRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.mailgroup_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListMailgroupManagerRequestBuilder":
        return ListMailgroupManagerRequestBuilder()


class ListMailgroupManagerRequestBuilder(object):

    def __init__(self,
                 list_mailgroup_manager_request: ListMailgroupManagerRequest = ListMailgroupManagerRequest()) -> None:
        list_mailgroup_manager_request.http_method = HttpMethod.GET
        list_mailgroup_manager_request.uri = "/open-apis/mail/v1/mailgroups/:mailgroup_id/managers"
        list_mailgroup_manager_request.token_types = {AccessTokenType.TENANT}
        self._list_mailgroup_manager_request: ListMailgroupManagerRequest = list_mailgroup_manager_request

    def page_size(self, page_size: int) -> "ListMailgroupManagerRequestBuilder":
        self._list_mailgroup_manager_request.page_size = page_size
        self._list_mailgroup_manager_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListMailgroupManagerRequestBuilder":
        self._list_mailgroup_manager_request.page_token = page_token
        self._list_mailgroup_manager_request.add_query("page_token", page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "ListMailgroupManagerRequestBuilder":
        self._list_mailgroup_manager_request.user_id_type = user_id_type
        self._list_mailgroup_manager_request.add_query("user_id_type", user_id_type)
        return self

    def mailgroup_id(self, mailgroup_id: str) -> "ListMailgroupManagerRequestBuilder":
        self._list_mailgroup_manager_request.mailgroup_id = mailgroup_id
        self._list_mailgroup_manager_request.paths["mailgroup_id"] = str(mailgroup_id)
        return self

    def build(self) -> ListMailgroupManagerRequest:
        return self._list_mailgroup_manager_request
