# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .di_data import DiData


class DiInfo(object):
    _types = {
        "id": str,
        "application_id": str,
        "talent_id": str,
        "source_type": int,
        "create_time": str,
        "update_time": str,
        "di_data": List[DiData],
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.application_id: Optional[str] = None
        self.talent_id: Optional[str] = None
        self.source_type: Optional[int] = None
        self.create_time: Optional[str] = None
        self.update_time: Optional[str] = None
        self.di_data: Optional[List[DiData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DiInfoBuilder":
        return DiInfoBuilder()


class DiInfoBuilder(object):
    def __init__(self, di_info: DiInfo = DiInfo({})) -> None:
        self._di_info: DiInfo = di_info

    def id(self, id: str) -> "DiInfoBuilder":
        self._di_info.id = id
        return self

    def application_id(self, application_id: str) -> "DiInfoBuilder":
        self._di_info.application_id = application_id
        return self

    def talent_id(self, talent_id: str) -> "DiInfoBuilder":
        self._di_info.talent_id = talent_id
        return self

    def source_type(self, source_type: int) -> "DiInfoBuilder":
        self._di_info.source_type = source_type
        return self

    def create_time(self, create_time: str) -> "DiInfoBuilder":
        self._di_info.create_time = create_time
        return self

    def update_time(self, update_time: str) -> "DiInfoBuilder":
        self._di_info.update_time = update_time
        return self

    def di_data(self, di_data: List[DiData]) -> "DiInfoBuilder":
        self._di_info.di_data = di_data
        return self

    def build(self) -> "DiInfo":
        return self._di_info