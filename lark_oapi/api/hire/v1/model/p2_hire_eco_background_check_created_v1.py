# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .eco_background_check_create_event_candidate_info import EcoBackgroundCheckCreateEventCandidateInfo
from .eco_background_check_create_event_contact_info import EcoBackgroundCheckCreateEventContactInfo
from .eco_background_check_create_event_custom_kv import EcoBackgroundCheckCreateEventCustomKv


class P2HireEcoBackgroundCheckCreatedV1Data(object):
    _types = {
        "background_check_id": str,
        "account_id": str,
        "package_id": str,
        "additional_item_id_list": List[str],
        "comment": str,
        "candidate_info": EcoBackgroundCheckCreateEventCandidateInfo,
        "client_contact_info": EcoBackgroundCheckCreateEventContactInfo,
        "custom_field_list": List[EcoBackgroundCheckCreateEventCustomKv],
    }

    def __init__(self, d=None):
        self.background_check_id: Optional[str] = None
        self.account_id: Optional[str] = None
        self.package_id: Optional[str] = None
        self.additional_item_id_list: Optional[List[str]] = None
        self.comment: Optional[str] = None
        self.candidate_info: Optional[EcoBackgroundCheckCreateEventCandidateInfo] = None
        self.client_contact_info: Optional[EcoBackgroundCheckCreateEventContactInfo] = None
        self.custom_field_list: Optional[List[EcoBackgroundCheckCreateEventCustomKv]] = None
        init(self, d, self._types)


class P2HireEcoBackgroundCheckCreatedV1(EventContext):
    _types = {
        "event": P2HireEcoBackgroundCheckCreatedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2HireEcoBackgroundCheckCreatedV1Data] = None
        init(self, d, self._types)