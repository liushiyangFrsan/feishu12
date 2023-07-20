# Code generated by Lark OpenAPI.

from .v3.resource import *


class ContactService(object):
    def __init__(self, config: Config) -> None:
        self.v3: V3 = V3(config)


class V3(object):
    def __init__(self, config: Config) -> None:
        self.custom_attr: Optional[CustomAttr] = CustomAttr(config)
        self.custom_attr_event: Optional[CustomAttrEvent] = CustomAttrEvent(config)
        self.department: Optional[Department] = Department(config)
        self.employee_type_enum: Optional[EmployeeTypeEnum] = EmployeeTypeEnum(config)
        self.functional_role: Optional[FunctionalRole] = FunctionalRole(config)
        self.functional_role_member: Optional[FunctionalRoleMember] = FunctionalRoleMember(config)
        self.group: Optional[Group] = Group(config)
        self.group_member: Optional[GroupMember] = GroupMember(config)
        self.job_family: Optional[JobFamily] = JobFamily(config)
        self.job_level: Optional[JobLevel] = JobLevel(config)
        self.job_title: Optional[JobTitle] = JobTitle(config)
        self.scope: Optional[Scope] = Scope(config)
        self.unit: Optional[Unit] = Unit(config)
        self.user: Optional[User] = User(config)
        self.work_city: Optional[WorkCity] = WorkCity(config)
