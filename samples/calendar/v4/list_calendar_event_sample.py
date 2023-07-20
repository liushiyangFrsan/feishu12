# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.calendar.v4 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListCalendarEventRequest = ListCalendarEventRequest.builder() \
        .calendar_id("feishu.cn_xxxxxxxxxx@group.calendar.feishu.cn") \
        .page_size(500) \
        .anchor_time("1609430400") \
        .page_token("ListCalendarsPageToken_1632452910_1632539310") \
        .sync_token("ListCalendarsSyncToken_1632452910") \
        .start_time("1631777271") \
        .end_time("1631777271") \
        .build()

    # 发起请求
    response: ListCalendarEventResponse = client.calendar.v4.calendar_event.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.calendar.v4.calendar_event.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
