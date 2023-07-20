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
    request: CreateApprovalRequest = CreateApprovalRequest.builder() \
        .department_id_type("open_department_id") \
        .user_id_type("user_id") \
        .request_body(ApprovalCreate.builder()
                      .approval_name("@i18n@approval_name")
                      .approval_code("7C468A54-8745-2245-9675-08B7C63E7A85")
                      .description("@i18n@description")
                      .viewers([])
                      .form(ApprovalForm.builder().build())
                      .node_list([])
                      .settings(ApprovalSetting.builder().build())
                      .config(ApprovalConfig.builder().build())
                      .icon(0)
                      .i18n_resources([])
                      .process_manager_ids([])
                      .build()) \
        .build()

    # 发起请求
    response: CreateApprovalResponse = client.approval.v4.approval.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.approval.v4.approval.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
