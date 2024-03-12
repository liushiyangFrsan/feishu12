# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .dataengine_i18n import DataengineI18n
from .process_link import ProcessLink


class ProcessCcItem(object):
    _types = {
        "approver_id": str,
        "links": ProcessLink,
        "operator_id": str,
        "operator_name": DataengineI18n,
        "node_name": DataengineI18n,
        "create_time": str,
        "node_definition_id": str,
    }

    def __init__(self, d=None):
        self.approver_id: Optional[str] = None
        self.links: Optional[ProcessLink] = None
        self.operator_id: Optional[str] = None
        self.operator_name: Optional[DataengineI18n] = None
        self.node_name: Optional[DataengineI18n] = None
        self.create_time: Optional[str] = None
        self.node_definition_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProcessCcItemBuilder":
        return ProcessCcItemBuilder()


class ProcessCcItemBuilder(object):
    def __init__(self) -> None:
        self._process_cc_item = ProcessCcItem()

    def approver_id(self, approver_id: str) -> "ProcessCcItemBuilder":
        self._process_cc_item.approver_id = approver_id
        return self

    def links(self, links: ProcessLink) -> "ProcessCcItemBuilder":
        self._process_cc_item.links = links
        return self

    def operator_id(self, operator_id: str) -> "ProcessCcItemBuilder":
        self._process_cc_item.operator_id = operator_id
        return self

    def operator_name(self, operator_name: DataengineI18n) -> "ProcessCcItemBuilder":
        self._process_cc_item.operator_name = operator_name
        return self

    def node_name(self, node_name: DataengineI18n) -> "ProcessCcItemBuilder":
        self._process_cc_item.node_name = node_name
        return self

    def create_time(self, create_time: str) -> "ProcessCcItemBuilder":
        self._process_cc_item.create_time = create_time
        return self

    def node_definition_id(self, node_definition_id: str) -> "ProcessCcItemBuilder":
        self._process_cc_item.node_definition_id = node_definition_id
        return self

    def build(self) -> "ProcessCcItem":
        return self._process_cc_item