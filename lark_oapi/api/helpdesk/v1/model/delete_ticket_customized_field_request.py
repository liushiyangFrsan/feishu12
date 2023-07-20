# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteTicketCustomizedFieldRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.ticket_customized_field_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteTicketCustomizedFieldRequestBuilder":
        return DeleteTicketCustomizedFieldRequestBuilder()


class DeleteTicketCustomizedFieldRequestBuilder(object):

    def __init__(self,
                 delete_ticket_customized_field_request: DeleteTicketCustomizedFieldRequest = DeleteTicketCustomizedFieldRequest()) -> None:
        delete_ticket_customized_field_request.http_method = HttpMethod.DELETE
        delete_ticket_customized_field_request.uri = "/open-apis/helpdesk/v1/ticket_customized_fields/:ticket_customized_field_id"
        delete_ticket_customized_field_request.token_types = {AccessTokenType.USER}
        self._delete_ticket_customized_field_request: DeleteTicketCustomizedFieldRequest = delete_ticket_customized_field_request

    def ticket_customized_field_id(self,
                                   ticket_customized_field_id: str) -> "DeleteTicketCustomizedFieldRequestBuilder":
        self._delete_ticket_customized_field_request.ticket_customized_field_id = ticket_customized_field_id
        self._delete_ticket_customized_field_request.paths["ticket_customized_field_id"] = str(
            ticket_customized_field_id)
        return self

    def build(self) -> DeleteTicketCustomizedFieldRequest:
        return self._delete_ticket_customized_field_request
