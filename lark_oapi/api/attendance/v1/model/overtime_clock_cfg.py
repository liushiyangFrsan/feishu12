# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class OvertimeClockCfg(object):
    _types = {
        "allow_punch_approval": bool,
        "need_clock_over_time_start_and_end": bool,
    }

    def __init__(self, d=None):
        self.allow_punch_approval: Optional[bool] = None
        self.need_clock_over_time_start_and_end: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OvertimeClockCfgBuilder":
        return OvertimeClockCfgBuilder()


class OvertimeClockCfgBuilder(object):
    def __init__(self) -> None:
        self._overtime_clock_cfg = OvertimeClockCfg()

    def allow_punch_approval(self, allow_punch_approval: bool) -> "OvertimeClockCfgBuilder":
        self._overtime_clock_cfg.allow_punch_approval = allow_punch_approval
        return self

    def need_clock_over_time_start_and_end(self, need_clock_over_time_start_and_end: bool) -> "OvertimeClockCfgBuilder":
        self._overtime_clock_cfg.need_clock_over_time_start_and_end = need_clock_over_time_start_and_end
        return self

    def build(self) -> "OvertimeClockCfg":
        return self._overtime_clock_cfg