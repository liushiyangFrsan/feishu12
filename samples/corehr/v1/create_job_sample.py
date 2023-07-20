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
    request: CreateJobRequest = CreateJobRequest.builder() \
        .client_token("12454646") \
        .request_body(Job.builder()
                      .code("JP422119")
                      .name([])
                      .description([])
                      .active(True)
                      .job_title([])
                      .job_family_id_list([])
                      .job_level_id_list([])
                      .working_hours_type_id("6890452208593372679")
                      .effective_time("2020-01-01 00:00:00")
                      .expiration_time("2021-01-01 00:00:00")
                      .custom_fields([])
                      .build()) \
        .build()

    # 发起请求
    response: CreateJobResponse = client.corehr.v1.job.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v1.job.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
