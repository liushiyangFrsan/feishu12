# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .chat_menu_item import ChatMenuItem


class ChatMenuSecondLevel(object):
    _types = {
        "chat_menu_second_level_id": int,
        "chat_menu_item": ChatMenuItem,
    }

    def __init__(self, d):
        self.chat_menu_second_level_id: Optional[int] = None
        self.chat_menu_item: Optional[ChatMenuItem] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChatMenuSecondLevelBuilder":
        return ChatMenuSecondLevelBuilder()


class ChatMenuSecondLevelBuilder(object):
    def __init__(self, chat_menu_second_level: ChatMenuSecondLevel = ChatMenuSecondLevel({})) -> None:
        self._chat_menu_second_level: ChatMenuSecondLevel = chat_menu_second_level

    def chat_menu_second_level_id(self, chat_menu_second_level_id: int) -> "ChatMenuSecondLevelBuilder":
        self._chat_menu_second_level.chat_menu_second_level_id = chat_menu_second_level_id
        return self

    def chat_menu_item(self, chat_menu_item: ChatMenuItem) -> "ChatMenuSecondLevelBuilder":
        self._chat_menu_second_level.chat_menu_item = chat_menu_item
        return self

    def build(self) -> "ChatMenuSecondLevel":
        return self._chat_menu_second_level