# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class QuerySpreadsheetSheetFilterViewRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.spreadsheet_token: Optional[str] = None
        self.sheet_id: Optional[str] = None

    @staticmethod
    def builder() -> "QuerySpreadsheetSheetFilterViewRequestBuilder":
        return QuerySpreadsheetSheetFilterViewRequestBuilder()


class QuerySpreadsheetSheetFilterViewRequestBuilder(object):

    def __init__(self,
                 query_spreadsheet_sheet_filter_view_request: QuerySpreadsheetSheetFilterViewRequest = QuerySpreadsheetSheetFilterViewRequest()) -> None:
        query_spreadsheet_sheet_filter_view_request.http_method = HttpMethod.GET
        query_spreadsheet_sheet_filter_view_request.uri = "/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/query"
        query_spreadsheet_sheet_filter_view_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._query_spreadsheet_sheet_filter_view_request: QuerySpreadsheetSheetFilterViewRequest = query_spreadsheet_sheet_filter_view_request

    def spreadsheet_token(self, spreadsheet_token: str) -> "QuerySpreadsheetSheetFilterViewRequestBuilder":
        self._query_spreadsheet_sheet_filter_view_request.spreadsheet_token = spreadsheet_token
        self._query_spreadsheet_sheet_filter_view_request.paths["spreadsheet_token"] = str(spreadsheet_token)
        return self

    def sheet_id(self, sheet_id: str) -> "QuerySpreadsheetSheetFilterViewRequestBuilder":
        self._query_spreadsheet_sheet_filter_view_request.sheet_id = sheet_id
        self._query_spreadsheet_sheet_filter_view_request.paths["sheet_id"] = str(sheet_id)
        return self

    def build(self) -> QuerySpreadsheetSheetFilterViewRequest:
        return self._query_spreadsheet_sheet_filter_view_request
