# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteWorkingHoursTypeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.working_hours_type_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteWorkingHoursTypeRequestBuilder":
        return DeleteWorkingHoursTypeRequestBuilder()


class DeleteWorkingHoursTypeRequestBuilder(object):

    def __init__(self,
                 delete_working_hours_type_request: DeleteWorkingHoursTypeRequest = DeleteWorkingHoursTypeRequest()) -> None:
        delete_working_hours_type_request.http_method = HttpMethod.DELETE
        delete_working_hours_type_request.uri = "/open-apis/corehr/v1/working_hours_types/:working_hours_type_id"
        delete_working_hours_type_request.token_types = {AccessTokenType.TENANT}
        self._delete_working_hours_type_request: DeleteWorkingHoursTypeRequest = delete_working_hours_type_request

    def working_hours_type_id(self, working_hours_type_id: str) -> "DeleteWorkingHoursTypeRequestBuilder":
        self._delete_working_hours_type_request.working_hours_type_id = working_hours_type_id
        self._delete_working_hours_type_request.paths["working_hours_type_id"] = str(working_hours_type_id)
        return self

    def build(self) -> DeleteWorkingHoursTypeRequest:
        return self._delete_working_hours_type_request
