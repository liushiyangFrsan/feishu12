# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .event_uid import EventUid


class EventUids(object):
    _types = {
        "event_uids": List[EventUid],
    }

    def __init__(self, d):
        self.event_uids: Optional[List[EventUid]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EventUidsBuilder":
        return EventUidsBuilder()


class EventUidsBuilder(object):
    def __init__(self, event_uids: EventUids = EventUids({})) -> None:
        self._event_uids: EventUids = event_uids
    
    def event_uids(self, event_uids: List[EventUid]) -> "EventUidsBuilder":
        self._event_uids.event_uids = event_uids
        return self
    
    def build(self) -> "EventUids":
        return self._event_uids