# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .eco_exam_create_event_candidate_info import EcoExamCreateEventCandidateInfo


class P2HireEcoExamCreatedV1Data(object):
    _types = {
        "exam_id": str,
        "account_id": str,
        "paper_id": str,
        "candidate_info": EcoExamCreateEventCandidateInfo,
    }

    def __init__(self, d=None):
        self.exam_id: Optional[str] = None
        self.account_id: Optional[str] = None
        self.paper_id: Optional[str] = None
        self.candidate_info: Optional[EcoExamCreateEventCandidateInfo] = None
        init(self, d, self._types)


class P2HireEcoExamCreatedV1(EventContext):
    _types = {
        "event": P2HireEcoExamCreatedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2HireEcoExamCreatedV1Data] = None
        init(self, d, self._types)