# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.acs.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: PatchUserRequest = PatchUserRequest.builder() \
        .user_id("ou_7dab8a3d3cdcc9da365777c7ad535d62") \
        .user_id_type("user_id") \
        .request_body(User.builder()
                      .feature(Feature.builder().build())
                      .build()) \
        .build()

    # 发起请求
    response: PatchUserResponse = client.acs.v1.user.patch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.acs.v1.user.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
