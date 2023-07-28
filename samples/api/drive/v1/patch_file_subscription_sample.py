# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.drive.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: PatchFileSubscriptionRequest = PatchFileSubscriptionRequest.builder() \
        .file_token("doxcnxxxxxxxxxxxxxxxxxxxxxx") \
        .subscription_id("1234567890987654321") \
        .request_body(PatchFileSubscriptionRequestBody.builder()
                      .is_subscribe(True)
                      .file_type("doc")
                      .build()) \
        .build()

    # 发起请求
    response: PatchFileSubscriptionResponse = client.drive.v1.file_subscription.patch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.drive.v1.file_subscription.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()