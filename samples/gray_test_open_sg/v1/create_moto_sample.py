# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.gray_test_open_sg.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id("APP_ID") \
        .app_secret("APP_SECRET") \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateMotoRequest = CreateMotoRequest.builder() \
        .department_id_type("str") \
        .user_id_type("str") \
        .request_body(Level.builder()
                      .level("str")
                      .body("str")
                      .type("str")
                      .build()) \
        .build()

    # 发起请求
    response: CreateMotoResponse = client.gray_test_open_sg.v1.moto.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.gray_test_open_sg.v1.moto.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()