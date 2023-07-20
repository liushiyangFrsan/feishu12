# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class MeetingRoom(object):
    _types = {
        "room_id": int,
    }

    def __init__(self, d):
        self.room_id: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MeetingRoomBuilder":
        return MeetingRoomBuilder()


class MeetingRoomBuilder(object):
    def __init__(self, meeting_room: MeetingRoom = MeetingRoom({})) -> None:
        self._meeting_room: MeetingRoom = meeting_room
    
    def room_id(self, room_id: int) -> "MeetingRoomBuilder":
        self._meeting_room.room_id = room_id
        return self
    
    def build(self) -> "MeetingRoom":
        return self._meeting_room