# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.ehr.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: GetAttachmentRequest = GetAttachmentRequest.builder() \
        .token("09bf7b924f9a4a69875788891b5970d8") \
        .build()

    # 发起请求
    response: GetAttachmentResponse = client.ehr.v1.attachment.get(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.ehr.v1.attachment.get failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    f = open(f"file_path/{response.file_name}", "wb")
    f.write(response.file.read())
    f.close()


if __name__ == "__main__":
    main()
