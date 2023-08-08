# Code generated by Lark OpenAPI.

import io
from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from lark_oapi.core.utils import Files
from ..model.download_export_request import DownloadExportRequest
from ..model.download_export_response import DownloadExportResponse
from ..model.get_export_request import GetExportRequest
from ..model.get_export_response import GetExportResponse
from ..model.meeting_list_export_request import MeetingListExportRequest
from ..model.meeting_list_export_response import MeetingListExportResponse
from ..model.participant_list_export_request import ParticipantListExportRequest
from ..model.participant_list_export_response import ParticipantListExportResponse
from ..model.participant_quality_list_export_request import ParticipantQualityListExportRequest
from ..model.participant_quality_list_export_response import ParticipantQualityListExportResponse
from ..model.resource_reservation_list_export_request import ResourceReservationListExportRequest
from ..model.resource_reservation_list_export_response import ResourceReservationListExportResponse


class Export(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def download(self, request: DownloadExportRequest,
                 option: Optional[RequestOption] = None) -> DownloadExportResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 处理二进制流
        if resp.status_code == 200:
            response: DownloadExportResponse = DownloadExportResponse({})
            response.code = 0
            response.raw = resp
            response.file = io.BytesIO(resp.content)
            response.file_name = Files.parse_file_name(response.raw.header)
            return response

        # 反序列化
        response: DownloadExportResponse = JSON.unmarshal(str(resp.content, UTF_8), DownloadExportResponse)
        response.raw = resp

        return response

    def get(self, request: GetExportRequest, option: Optional[RequestOption] = None) -> GetExportResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: GetExportResponse = JSON.unmarshal(str(resp.content, UTF_8), GetExportResponse)
        response.raw = resp

        return response

    def meeting_list(self, request: MeetingListExportRequest,
                     option: Optional[RequestOption] = None) -> MeetingListExportResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: MeetingListExportResponse = JSON.unmarshal(str(resp.content, UTF_8), MeetingListExportResponse)
        response.raw = resp

        return response

    def participant_list(self, request: ParticipantListExportRequest,
                         option: Optional[RequestOption] = None) -> ParticipantListExportResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ParticipantListExportResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                 ParticipantListExportResponse)
        response.raw = resp

        return response

    def participant_quality_list(self, request: ParticipantQualityListExportRequest,
                                 option: Optional[RequestOption] = None) -> ParticipantQualityListExportResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ParticipantQualityListExportResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                        ParticipantQualityListExportResponse)
        response.raw = resp

        return response

    def resource_reservation_list(self, request: ResourceReservationListExportRequest,
                                  option: Optional[RequestOption] = None) -> ResourceReservationListExportResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ResourceReservationListExportResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                         ResourceReservationListExportResponse)
        response.raw = resp

        return response
