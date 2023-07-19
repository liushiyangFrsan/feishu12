# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_space_response_body import GetSpaceResponseBody


class GetSpaceResponse(BaseResponse):
    _types = {
        "data": GetSpaceResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetSpaceResponseBody] = None
        init(self, d, self._types)