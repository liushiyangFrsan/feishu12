# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: DeleteLeaveGrantingRecordRequest = DeleteLeaveGrantingRecordRequest.builder() \
        .leave_granting_record_id("6893014062142064135") \
        .build()

    # 发起请求
    response: DeleteLeaveGrantingRecordResponse = client.corehr.v1.leave_granting_record.delete(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v1.leave_granting_record.delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
