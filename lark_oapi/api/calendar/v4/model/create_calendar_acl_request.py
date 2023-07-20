# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .calendar_acl import CalendarAcl


class CreateCalendarAclRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.calendar_id: Optional[str] = None
        self.request_body: Optional[CalendarAcl] = None

    @staticmethod
    def builder() -> "CreateCalendarAclRequestBuilder":
        return CreateCalendarAclRequestBuilder()


class CreateCalendarAclRequestBuilder(object):

    def __init__(self, create_calendar_acl_request: CreateCalendarAclRequest = CreateCalendarAclRequest()) -> None:
        create_calendar_acl_request.http_method = HttpMethod.POST
        create_calendar_acl_request.uri = "/open-apis/calendar/v4/calendars/:calendar_id/acls"
        create_calendar_acl_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_calendar_acl_request: CreateCalendarAclRequest = create_calendar_acl_request

    def user_id_type(self, user_id_type: str) -> "CreateCalendarAclRequestBuilder":
        self._create_calendar_acl_request.user_id_type = user_id_type
        self._create_calendar_acl_request.add_query("user_id_type", user_id_type)
        return self

    def calendar_id(self, calendar_id: str) -> "CreateCalendarAclRequestBuilder":
        self._create_calendar_acl_request.calendar_id = calendar_id
        self._create_calendar_acl_request.paths["calendar_id"] = str(calendar_id)
        return self

    def request_body(self, request_body: CalendarAcl) -> "CreateCalendarAclRequestBuilder":
        self._create_calendar_acl_request.request_body = request_body
        self._create_calendar_acl_request.body = request_body
        return self

    def build(self) -> CreateCalendarAclRequest:
        return self._create_calendar_acl_request
