# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .recognized_entity import RecognizedEntity


class RecognizedEntities(object):
    _types = {
        "entities": List[RecognizedEntity],
    }

    def __init__(self, d=None):
        self.entities: Optional[List[RecognizedEntity]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RecognizedEntitiesBuilder":
        return RecognizedEntitiesBuilder()


class RecognizedEntitiesBuilder(object):
    def __init__(self) -> None:
        self._recognized_entities = RecognizedEntities()

    def entities(self, entities: List[RecognizedEntity]) -> "RecognizedEntitiesBuilder":
        self._recognized_entities.entities = entities
        return self

    def build(self) -> "RecognizedEntities":
        return self._recognized_entities