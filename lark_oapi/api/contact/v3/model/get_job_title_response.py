# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_job_title_response_body import GetJobTitleResponseBody


class GetJobTitleResponse(BaseResponse):
    _types = {
        "data": GetJobTitleResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[GetJobTitleResponseBody] = None
        init(self, d, self._types)
