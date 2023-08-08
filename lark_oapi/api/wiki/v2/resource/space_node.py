# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core import JSON
from lark_oapi.core.const import UTF_8
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.token import verify
from ..model.copy_space_node_request import CopySpaceNodeRequest
from ..model.copy_space_node_response import CopySpaceNodeResponse
from ..model.create_space_node_request import CreateSpaceNodeRequest
from ..model.create_space_node_response import CreateSpaceNodeResponse
from ..model.list_space_node_request import ListSpaceNodeRequest
from ..model.list_space_node_response import ListSpaceNodeResponse
from ..model.move_docs_to_wiki_space_node_request import MoveDocsToWikiSpaceNodeRequest
from ..model.move_docs_to_wiki_space_node_response import MoveDocsToWikiSpaceNodeResponse
from ..model.move_space_node_request import MoveSpaceNodeRequest
from ..model.move_space_node_response import MoveSpaceNodeResponse
from ..model.update_title_space_node_request import UpdateTitleSpaceNodeRequest
from ..model.update_title_space_node_response import UpdateTitleSpaceNodeResponse


class SpaceNode(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def copy(self, request: CopySpaceNodeRequest, option: Optional[RequestOption] = None) -> CopySpaceNodeResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CopySpaceNodeResponse = JSON.unmarshal(str(resp.content, UTF_8), CopySpaceNodeResponse)
        response.raw = resp

        return response

    def create(self, request: CreateSpaceNodeRequest,
               option: Optional[RequestOption] = None) -> CreateSpaceNodeResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: CreateSpaceNodeResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateSpaceNodeResponse)
        response.raw = resp

        return response

    def list(self, request: ListSpaceNodeRequest, option: Optional[RequestOption] = None) -> ListSpaceNodeResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: ListSpaceNodeResponse = JSON.unmarshal(str(resp.content, UTF_8), ListSpaceNodeResponse)
        response.raw = resp

        return response

    def move(self, request: MoveSpaceNodeRequest, option: Optional[RequestOption] = None) -> MoveSpaceNodeResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: MoveSpaceNodeResponse = JSON.unmarshal(str(resp.content, UTF_8), MoveSpaceNodeResponse)
        response.raw = resp

        return response

    def move_docs_to_wiki(self, request: MoveDocsToWikiSpaceNodeRequest,
                          option: Optional[RequestOption] = None) -> MoveDocsToWikiSpaceNodeResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: MoveDocsToWikiSpaceNodeResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                   MoveDocsToWikiSpaceNodeResponse)
        response.raw = resp

        return response

    def update_title(self, request: UpdateTitleSpaceNodeRequest,
                     option: Optional[RequestOption] = None) -> UpdateTitleSpaceNodeResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: UpdateTitleSpaceNodeResponse = JSON.unmarshal(str(resp.content, UTF_8), UpdateTitleSpaceNodeResponse)
        response.raw = resp

        return response
