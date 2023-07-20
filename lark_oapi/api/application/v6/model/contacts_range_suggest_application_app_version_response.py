# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .contacts_range_suggest_application_app_version_response_body import ContactsRangeSuggestApplicationAppVersionResponseBody


class ContactsRangeSuggestApplicationAppVersionResponse(BaseResponse):
    _types = {
        "data": ContactsRangeSuggestApplicationAppVersionResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ContactsRangeSuggestApplicationAppVersionResponseBody] = None
        init(self, d, self._types)
