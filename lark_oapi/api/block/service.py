# Code generated by Lark OpenAPI.

from lark_oapi.core.model import Config
from .v2.version import V2


class BlockService(object):
    def __init__(self, config: Config) -> None:
        self.v2: V2 = V2(config)
