# -*- coding: UTF-8 -*-
# Code generated by lark suite oapi sdk gen

from typing import List, Dict, Any
from ....utils.dt import to_json_decorator
import attr




@to_json_decorator
@attr.s
class FaceVerify(object):
    pass




@attr.s
class FaceVerifyCropFaceImageResult(object):
    auth_state = attr.ib(type=int, default=None, metadata={'json': 'auth_state'})
    auth_timpstamp = attr.ib(type=int, default=None, metadata={'json': 'auth_timpstamp'})



@attr.s
class FaceVerifyQueryAuthResultResult(object):
    auth_state = attr.ib(type=int, default=None, metadata={'json': 'auth_state'})
    auth_timpstamp = attr.ib(type=int, default=None, metadata={'json': 'auth_timpstamp'})



@attr.s
class FaceVerifyUploadFaceImageResult(object):
    auth_state = attr.ib(type=int, default=None, metadata={'json': 'auth_state'})
    auth_timpstamp = attr.ib(type=int, default=None, metadata={'json': 'auth_timpstamp'})