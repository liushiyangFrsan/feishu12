# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class QuerySpreadsheetSheetFilterViewConditionRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.spreadsheet_token: Optional[str] = None
        self.sheet_id: Optional[str] = None
        self.filter_view_id: Optional[str] = None

    @staticmethod
    def builder() -> "QuerySpreadsheetSheetFilterViewConditionRequestBuilder":
        return QuerySpreadsheetSheetFilterViewConditionRequestBuilder()


class QuerySpreadsheetSheetFilterViewConditionRequestBuilder(object):

    def __init__(self,
                 query_spreadsheet_sheet_filter_view_condition_request: QuerySpreadsheetSheetFilterViewConditionRequest = QuerySpreadsheetSheetFilterViewConditionRequest()) -> None:
        query_spreadsheet_sheet_filter_view_condition_request.http_method = HttpMethod.GET
        query_spreadsheet_sheet_filter_view_condition_request.uri = "/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id/conditions/query"
        query_spreadsheet_sheet_filter_view_condition_request.token_types = {AccessTokenType.TENANT,
                                                                             AccessTokenType.USER}
        self._query_spreadsheet_sheet_filter_view_condition_request: QuerySpreadsheetSheetFilterViewConditionRequest = query_spreadsheet_sheet_filter_view_condition_request

    def spreadsheet_token(self, spreadsheet_token: str) -> "QuerySpreadsheetSheetFilterViewConditionRequestBuilder":
        self._query_spreadsheet_sheet_filter_view_condition_request.spreadsheet_token = spreadsheet_token
        self._query_spreadsheet_sheet_filter_view_condition_request.paths["spreadsheet_token"] = str(spreadsheet_token)
        return self

    def sheet_id(self, sheet_id: str) -> "QuerySpreadsheetSheetFilterViewConditionRequestBuilder":
        self._query_spreadsheet_sheet_filter_view_condition_request.sheet_id = sheet_id
        self._query_spreadsheet_sheet_filter_view_condition_request.paths["sheet_id"] = str(sheet_id)
        return self

    def filter_view_id(self, filter_view_id: str) -> "QuerySpreadsheetSheetFilterViewConditionRequestBuilder":
        self._query_spreadsheet_sheet_filter_view_condition_request.filter_view_id = filter_view_id
        self._query_spreadsheet_sheet_filter_view_condition_request.paths["filter_view_id"] = str(filter_view_id)
        return self

    def build(self) -> QuerySpreadsheetSheetFilterViewConditionRequest:
        return self._query_spreadsheet_sheet_filter_view_condition_request
