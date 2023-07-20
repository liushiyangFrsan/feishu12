# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.approval.v4 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListInstanceCommentRequest = ListInstanceCommentRequest.builder() \
        .instance_id("6A123516-FB88-470D-A428-9AF58B71B3C0") \
        .user_id_type("user_id") \
        .user_id("e5286g26") \
        .page_token("nF1ZXJ5VGhlbkZldGNoCgAAAAAA6PZwFmUzSldvTC1yU") \
        .page_size(10) \
        .build()

    # 发起请求
    response: ListInstanceCommentResponse = client.approval.v4.instance_comment.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.approval.v4.instance_comment.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
