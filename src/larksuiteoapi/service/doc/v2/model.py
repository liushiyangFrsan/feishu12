# -*- coding: UTF-8 -*-
# Code generated by lark suite oapi sdk gen

from typing import List, Dict, Any
from ....utils.dt import to_json_decorator
import attr




@to_json_decorator
@attr.s
class Doc(object):
    pass



@to_json_decorator
@attr.s
class DocBatchUpdateReqBody(object):
    doc_token = attr.ib(type=str, default=None, metadata={'json': 'docToken'})
    revision = attr.ib(type=int, default=None, metadata={'json': 'Revision'})
    requests = attr.ib(type=List[str], default=None, metadata={'json': 'Requests'})




@attr.s
class DocContentResult(object):
    content = attr.ib(type=str, default=None, metadata={'json': 'content'})
    revision = attr.ib(type=int, default=None, metadata={'json': 'revision'})


@to_json_decorator
@attr.s
class DocCreateReqBody(object):
    folder_token = attr.ib(type=str, default=None, metadata={'json': 'FolderToken'})
    content = attr.ib(type=str, default=None, metadata={'json': 'Content'})


@attr.s
class DocCreateResult(object):
    obj_token = attr.ib(type=str, default=None, metadata={'json': 'objToken'})
    url = attr.ib(type=str, default=None, metadata={'json': 'url'})



@attr.s
class DocMetaResult(object):
    create_date = attr.ib(type=str, default=None, metadata={'json': 'create_date'})
    create_time = attr.ib(type=int, default=None, metadata={'json': 'create_time'})
    creator = attr.ib(type=str, default=None, metadata={'json': 'creator'})
    create_user_name = attr.ib(type=str, default=None, metadata={'json': 'create_user_name'})
    delete_flag = attr.ib(type=int, default=None, metadata={'json': 'delete_flag'})
    edit_time = attr.ib(type=int, default=None, metadata={'json': 'edit_time'})
    edit_user_name = attr.ib(type=str, default=None, metadata={'json': 'edit_user_name'})
    is_external = attr.ib(type=bool, default=None, metadata={'json': 'is_external'})
    is_pined = attr.ib(type=bool, default=None, metadata={'json': 'is_pined'})
    is_stared = attr.ib(type=bool, default=None, metadata={'json': 'is_stared'})
    obj_type = attr.ib(type=str, default=None, metadata={'json': 'obj_type'})
    owner = attr.ib(type=str, default=None, metadata={'json': 'owner'})
    owner_user_name = attr.ib(type=str, default=None, metadata={'json': 'owner_user_name'})
    server_time = attr.ib(type=int, default=None, metadata={'json': 'server_time'})
    tenant_id = attr.ib(type=str, default=None, metadata={'json': 'tenant_id'})
    title = attr.ib(type=str, default=None, metadata={'json': 'title'})
    type = attr.ib(type=int, default=None, metadata={'json': 'type'})
    url = attr.ib(type=str, default=None, metadata={'json': 'url'})



@attr.s
class DocRawContentResult(object):
    content = attr.ib(type=str, default=None, metadata={'json': 'content'})