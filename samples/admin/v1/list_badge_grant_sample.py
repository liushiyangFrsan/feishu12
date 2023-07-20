# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.admin.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListBadgeGrantRequest = ListBadgeGrantRequest.builder() \
        .badge_id("m_DjMzaK") \
        .page_size(10) \
        .page_token("om5fn1") \
        .user_id_type("open_id") \
        .department_id_type("open_department_id") \
        .name("激励勋章的授予名单") \
        .build()

    # 发起请求
    response: ListBadgeGrantResponse = client.admin.v1.badge_grant.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.admin.v1.badge_grant.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
