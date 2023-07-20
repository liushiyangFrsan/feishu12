# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.attendance.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: QueryUserDailyShiftRequest = QueryUserDailyShiftRequest.builder() \
        .employee_type("employee_id") \
        .request_body(QueryUserDailyShiftRequestBody.builder()
                      .user_ids([])
                      .check_date_from(20190817)
                      .check_date_to(20190820)
                      .build()) \
        .build()

    # 发起请求
    response: QueryUserDailyShiftResponse = client.attendance.v1.user_daily_shift.query(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.attendance.v1.user_daily_shift.query failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
