# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetFunctionalRoleMemberRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.department_id_type: Optional[str] = None
        self.role_id: Optional[str] = None
        self.member_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetFunctionalRoleMemberRequestBuilder":
        return GetFunctionalRoleMemberRequestBuilder()


class GetFunctionalRoleMemberRequestBuilder(object):

    def __init__(self,
                 get_functional_role_member_request: GetFunctionalRoleMemberRequest = GetFunctionalRoleMemberRequest()) -> None:
        get_functional_role_member_request.http_method = HttpMethod.GET
        get_functional_role_member_request.uri = "/open-apis/contact/v3/functional_roles/:role_id/members/:member_id"
        get_functional_role_member_request.token_types = {AccessTokenType.TENANT}
        self._get_functional_role_member_request: GetFunctionalRoleMemberRequest = get_functional_role_member_request

    def user_id_type(self, user_id_type: str) -> "GetFunctionalRoleMemberRequestBuilder":
        self._get_functional_role_member_request.user_id_type = user_id_type
        self._get_functional_role_member_request.add_query("user_id_type", user_id_type)
        return self

    def department_id_type(self, department_id_type: str) -> "GetFunctionalRoleMemberRequestBuilder":
        self._get_functional_role_member_request.department_id_type = department_id_type
        self._get_functional_role_member_request.add_query("department_id_type", department_id_type)
        return self

    def role_id(self, role_id: str) -> "GetFunctionalRoleMemberRequestBuilder":
        self._get_functional_role_member_request.role_id = role_id
        self._get_functional_role_member_request.paths["role_id"] = str(role_id)
        return self

    def member_id(self, member_id: str) -> "GetFunctionalRoleMemberRequestBuilder":
        self._get_functional_role_member_request.member_id = member_id
        self._get_functional_role_member_request.paths["member_id"] = str(member_id)
        return self

    def build(self) -> GetFunctionalRoleMemberRequest:
        return self._get_functional_role_member_request
