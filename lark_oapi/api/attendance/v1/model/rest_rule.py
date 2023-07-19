# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class RestRule(object):
    _types = {
        "rest_begin_time": str,
        "rest_end_time": str,
    }

    def __init__(self, d):
        self.rest_begin_time: Optional[str] = None
        self.rest_end_time: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RestRuleBuilder":
        return RestRuleBuilder()


class RestRuleBuilder(object):
    def __init__(self, rest_rule: RestRule = RestRule({})) -> None:
        self._rest_rule: RestRule = rest_rule

    def rest_begin_time(self, rest_begin_time: str) -> "RestRuleBuilder":
        self._rest_rule.rest_begin_time = rest_begin_time
        return self

    def rest_end_time(self, rest_end_time: str) -> "RestRuleBuilder":
        self._rest_rule.rest_end_time = rest_end_time
        return self

    def build(self) -> "RestRule":
        return self._rest_rule