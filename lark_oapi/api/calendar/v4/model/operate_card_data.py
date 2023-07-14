# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init


class OperateCardData(object):
    _types = {
        "meeting_url": str,
        "meeting_no": str,
    }

    def __init__(self, d):
        self.meeting_url: Optional[str] = None
        self.meeting_no: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OperateCardDataBuilder":
        return OperateCardDataBuilder()


class OperateCardDataBuilder(object):
    def __init__(self, operate_card_data: OperateCardData = OperateCardData({})) -> None:
        self._operate_card_data: OperateCardData = operate_card_data
    
    def meeting_url(self, meeting_url: str) -> "OperateCardDataBuilder":
        self._operate_card_data.meeting_url = meeting_url
        return self
    
    def meeting_no(self, meeting_no: str) -> "OperateCardDataBuilder":
        self._operate_card_data.meeting_no = meeting_no
        return self
    
    def build(self) -> "OperateCardData":
        return self._operate_card_data