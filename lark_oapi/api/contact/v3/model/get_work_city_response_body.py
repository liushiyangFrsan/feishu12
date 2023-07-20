# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .work_city import WorkCity


class GetWorkCityResponseBody(object):
    _types = {
        "work_city": WorkCity,
    }

    def __init__(self, d):
        self.work_city: Optional[WorkCity] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetWorkCityResponseBodyBuilder":
        return GetWorkCityResponseBodyBuilder()


class GetWorkCityResponseBodyBuilder(object):
    def __init__(self, get_work_city_response_body: GetWorkCityResponseBody = GetWorkCityResponseBody({})) -> None:
        self._get_work_city_response_body: GetWorkCityResponseBody = get_work_city_response_body

    def work_city(self, work_city: WorkCity) -> "GetWorkCityResponseBodyBuilder":
        self._get_work_city_response_body.work_city = work_city
        return self

    def build(self) -> "GetWorkCityResponseBody":
        return self._get_work_city_response_body
