# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.vc.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: GetScopeConfigRequest = GetScopeConfigRequest.builder() \
        .scope_type(1) \
        .scope_id("omm_608d34d82d531b27fa993902d350a307") \
        .user_id_type("user_id") \
        .build()

    # 发起请求
    response: GetScopeConfigResponse = client.vc.v1.scope_config.get(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.scope_config.get failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
