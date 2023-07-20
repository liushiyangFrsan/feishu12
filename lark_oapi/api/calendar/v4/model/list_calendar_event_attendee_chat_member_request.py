# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListCalendarEventAttendeeChatMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        self.user_id_type: Optional[str] = None
        self.calendar_id: Optional[str] = None
        self.event_id: Optional[str] = None
        self.attendee_id: Optional[str] = None

    @staticmethod
    def builder() -> "ListCalendarEventAttendeeChatMemberRequestBuilder":
        return ListCalendarEventAttendeeChatMemberRequestBuilder()


class ListCalendarEventAttendeeChatMemberRequestBuilder(object):

    def __init__(self,
                 list_calendar_event_attendee_chat_member_request: ListCalendarEventAttendeeChatMemberRequest = ListCalendarEventAttendeeChatMemberRequest()) -> None:
        list_calendar_event_attendee_chat_member_request.http_method = HttpMethod.GET
        list_calendar_event_attendee_chat_member_request.uri = "/open-apis/calendar/v4/calendars/:calendar_id/events/:event_id/attendees/:attendee_id/chat_members"
        list_calendar_event_attendee_chat_member_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._list_calendar_event_attendee_chat_member_request: ListCalendarEventAttendeeChatMemberRequest = list_calendar_event_attendee_chat_member_request

    def page_token(self, page_token: str) -> "ListCalendarEventAttendeeChatMemberRequestBuilder":
        self._list_calendar_event_attendee_chat_member_request.page_token = page_token
        self._list_calendar_event_attendee_chat_member_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListCalendarEventAttendeeChatMemberRequestBuilder":
        self._list_calendar_event_attendee_chat_member_request.page_size = page_size
        self._list_calendar_event_attendee_chat_member_request.add_query("page_size", page_size)
        return self

    def user_id_type(self, user_id_type: str) -> "ListCalendarEventAttendeeChatMemberRequestBuilder":
        self._list_calendar_event_attendee_chat_member_request.user_id_type = user_id_type
        self._list_calendar_event_attendee_chat_member_request.add_query("user_id_type", user_id_type)
        return self

    def calendar_id(self, calendar_id: str) -> "ListCalendarEventAttendeeChatMemberRequestBuilder":
        self._list_calendar_event_attendee_chat_member_request.calendar_id = calendar_id
        self._list_calendar_event_attendee_chat_member_request.paths["calendar_id"] = str(calendar_id)
        return self

    def event_id(self, event_id: str) -> "ListCalendarEventAttendeeChatMemberRequestBuilder":
        self._list_calendar_event_attendee_chat_member_request.event_id = event_id
        self._list_calendar_event_attendee_chat_member_request.paths["event_id"] = str(event_id)
        return self

    def attendee_id(self, attendee_id: str) -> "ListCalendarEventAttendeeChatMemberRequestBuilder":
        self._list_calendar_event_attendee_chat_member_request.attendee_id = attendee_id
        self._list_calendar_event_attendee_chat_member_request.paths["attendee_id"] = str(attendee_id)
        return self

    def build(self) -> ListCalendarEventAttendeeChatMemberRequest:
        return self._list_calendar_event_attendee_chat_member_request
