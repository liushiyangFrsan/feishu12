# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetParticipantListRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.meeting_start_time: Optional[int] = None
        self.meeting_end_time: Optional[int] = None
        self.meeting_no: Optional[str] = None
        self.user_id: Optional[str] = None
        self.room_id: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.user_id_type: Optional[str] = None

    @staticmethod
    def builder() -> "GetParticipantListRequestBuilder":
        return GetParticipantListRequestBuilder()


class GetParticipantListRequestBuilder(object):

    def __init__(self, get_participant_list_request: GetParticipantListRequest = GetParticipantListRequest()) -> None:
        get_participant_list_request.http_method = HttpMethod.GET
        get_participant_list_request.uri = "/open-apis/vc/v1/participant_list"
        get_participant_list_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_participant_list_request: GetParticipantListRequest = get_participant_list_request

    def meeting_start_time(self, meeting_start_time: int) -> "GetParticipantListRequestBuilder":
        self._get_participant_list_request.meeting_start_time = meeting_start_time
        self._get_participant_list_request.queries["meeting_start_time"] = str(meeting_start_time)
        return self

    def meeting_end_time(self, meeting_end_time: int) -> "GetParticipantListRequestBuilder":
        self._get_participant_list_request.meeting_end_time = meeting_end_time
        self._get_participant_list_request.queries["meeting_end_time"] = str(meeting_end_time)
        return self

    def meeting_no(self, meeting_no: str) -> "GetParticipantListRequestBuilder":
        self._get_participant_list_request.meeting_no = meeting_no
        self._get_participant_list_request.queries["meeting_no"] = str(meeting_no)
        return self

    def user_id(self, user_id: str) -> "GetParticipantListRequestBuilder":
        self._get_participant_list_request.user_id = user_id
        self._get_participant_list_request.queries["user_id"] = str(user_id)
        return self

    def room_id(self, room_id: str) -> "GetParticipantListRequestBuilder":
        self._get_participant_list_request.room_id = room_id
        self._get_participant_list_request.queries["room_id"] = str(room_id)
        return self

    def page_size(self, page_size: int) -> "GetParticipantListRequestBuilder":
        self._get_participant_list_request.page_size = page_size
        self._get_participant_list_request.queries["page_size"] = str(page_size)
        return self

    def page_token(self, page_token: str) -> "GetParticipantListRequestBuilder":
        self._get_participant_list_request.page_token = page_token
        self._get_participant_list_request.queries["page_token"] = str(page_token)
        return self

    def user_id_type(self, user_id_type: str) -> "GetParticipantListRequestBuilder":
        self._get_participant_list_request.user_id_type = user_id_type
        self._get_participant_list_request.queries["user_id_type"] = str(user_id_type)
        return self

    def build(self) -> GetParticipantListRequest:
        return self._get_participant_list_request