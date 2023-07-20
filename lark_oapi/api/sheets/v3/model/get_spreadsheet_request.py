# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetSpreadsheetRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.spreadsheet_token: Optional[str] = None

    @staticmethod
    def builder() -> "GetSpreadsheetRequestBuilder":
        return GetSpreadsheetRequestBuilder()


class GetSpreadsheetRequestBuilder(object):

    def __init__(self, get_spreadsheet_request: GetSpreadsheetRequest = GetSpreadsheetRequest()) -> None:
        get_spreadsheet_request.http_method = HttpMethod.GET
        get_spreadsheet_request.uri = "/open-apis/sheets/v3/spreadsheets/:spreadsheet_token"
        get_spreadsheet_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_spreadsheet_request: GetSpreadsheetRequest = get_spreadsheet_request

    def user_id_type(self, user_id_type: str) -> "GetSpreadsheetRequestBuilder":
        self._get_spreadsheet_request.user_id_type = user_id_type
        self._get_spreadsheet_request.add_query("user_id_type", user_id_type)
        return self

    def spreadsheet_token(self, spreadsheet_token: str) -> "GetSpreadsheetRequestBuilder":
        self._get_spreadsheet_request.spreadsheet_token = spreadsheet_token
        self._get_spreadsheet_request.paths["spreadsheet_token"] = str(spreadsheet_token)
        return self

    def build(self) -> GetSpreadsheetRequest:
        return self._get_spreadsheet_request
