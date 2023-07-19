# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .query_session_response_body import QuerySessionResponseBody


class QuerySessionResponse(BaseResponse):
    _types = {
        "data": QuerySessionResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[QuerySessionResponseBody] = None
        init(self, d, self._types)