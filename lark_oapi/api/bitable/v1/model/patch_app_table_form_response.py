# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_app_table_form_response_body import PatchAppTableFormResponseBody


class PatchAppTableFormResponse(BaseResponse):
    _types = {
        "data": PatchAppTableFormResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[PatchAppTableFormResponseBody] = None
        init(self, d, self._types)