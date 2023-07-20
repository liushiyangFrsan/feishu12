# Code generated by Lark OpenAPI.

from lark_oapi.core.model import Config
from .v1.resource import *


class TranslationService(object):
    def __init__(self, config: Config) -> None:
        self.v1: V1 = V1(config)


class V1(object):
    def __init__(self, config: Config) -> None:
        self.text: Optional[Text] = Text(config)