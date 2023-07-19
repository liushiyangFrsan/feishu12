# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .calendar_event import CalendarEvent


class SearchCalendarEventResponseBody(object):
    _types = {
        "items": List[CalendarEvent],
        "page_token": str,
    }

    def __init__(self, d):
        self.items: Optional[List[CalendarEvent]] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchCalendarEventResponseBodyBuilder":
        return SearchCalendarEventResponseBodyBuilder()


class SearchCalendarEventResponseBodyBuilder(object):
    def __init__(self,
                 search_calendar_event_response_body: SearchCalendarEventResponseBody = SearchCalendarEventResponseBody(
                     {})) -> None:
        self._search_calendar_event_response_body: SearchCalendarEventResponseBody = search_calendar_event_response_body

    def items(self, items: List[CalendarEvent]) -> "SearchCalendarEventResponseBodyBuilder":
        self._search_calendar_event_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "SearchCalendarEventResponseBodyBuilder":
        self._search_calendar_event_response_body.page_token = page_token
        return self

    def build(self) -> "SearchCalendarEventResponseBody":
        return self._search_calendar_event_response_body