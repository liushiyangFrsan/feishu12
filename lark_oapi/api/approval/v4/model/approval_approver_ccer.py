# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class ApprovalApproverCcer(object):
    _types = {
        "type": str,
        "user_id": str,
        "level": str,
    }

    def __init__(self, d):
        self.type: Optional[str] = None
        self.user_id: Optional[str] = None
        self.level: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ApprovalApproverCcerBuilder":
        return ApprovalApproverCcerBuilder()


class ApprovalApproverCcerBuilder(object):
    def __init__(self, approval_approver_ccer: ApprovalApproverCcer = ApprovalApproverCcer({})) -> None:
        self._approval_approver_ccer: ApprovalApproverCcer = approval_approver_ccer

    def type(self, type: str) -> "ApprovalApproverCcerBuilder":
        self._approval_approver_ccer.type = type
        return self

    def user_id(self, user_id: str) -> "ApprovalApproverCcerBuilder":
        self._approval_approver_ccer.user_id = user_id
        return self

    def level(self, level: str) -> "ApprovalApproverCcerBuilder":
        self._approval_approver_ccer.level = level
        return self

    def build(self) -> "ApprovalApproverCcer":
        return self._approval_approver_ccer