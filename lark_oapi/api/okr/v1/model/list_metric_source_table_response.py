# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_metric_source_table_response_body import ListMetricSourceTableResponseBody


class ListMetricSourceTableResponse(BaseResponse):
    _types = {
        "data": ListMetricSourceTableResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListMetricSourceTableResponseBody] = None
        init(self, d, self._types)