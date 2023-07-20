# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .float_image import FloatImage


class CreateSpreadsheetSheetFloatImageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.spreadsheet_token: Optional[str] = None
        self.sheet_id: Optional[str] = None
        self.request_body: Optional[FloatImage] = None

    @staticmethod
    def builder() -> "CreateSpreadsheetSheetFloatImageRequestBuilder":
        return CreateSpreadsheetSheetFloatImageRequestBuilder()


class CreateSpreadsheetSheetFloatImageRequestBuilder(object):

    def __init__(self,
                 create_spreadsheet_sheet_float_image_request: CreateSpreadsheetSheetFloatImageRequest = CreateSpreadsheetSheetFloatImageRequest()) -> None:
        create_spreadsheet_sheet_float_image_request.http_method = HttpMethod.POST
        create_spreadsheet_sheet_float_image_request.uri = "/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/float_images"
        create_spreadsheet_sheet_float_image_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._create_spreadsheet_sheet_float_image_request: CreateSpreadsheetSheetFloatImageRequest = create_spreadsheet_sheet_float_image_request

    def spreadsheet_token(self, spreadsheet_token: str) -> "CreateSpreadsheetSheetFloatImageRequestBuilder":
        self._create_spreadsheet_sheet_float_image_request.spreadsheet_token = spreadsheet_token
        self._create_spreadsheet_sheet_float_image_request.paths["spreadsheet_token"] = str(spreadsheet_token)
        return self

    def sheet_id(self, sheet_id: str) -> "CreateSpreadsheetSheetFloatImageRequestBuilder":
        self._create_spreadsheet_sheet_float_image_request.sheet_id = sheet_id
        self._create_spreadsheet_sheet_float_image_request.paths["sheet_id"] = str(sheet_id)
        return self

    def request_body(self, request_body: FloatImage) -> "CreateSpreadsheetSheetFloatImageRequestBuilder":
        self._create_spreadsheet_sheet_float_image_request.request_body = request_body
        self._create_spreadsheet_sheet_float_image_request.body = request_body
        return self

    def build(self) -> CreateSpreadsheetSheetFloatImageRequest:
        return self._create_spreadsheet_sheet_float_image_request
