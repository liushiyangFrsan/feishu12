# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.docx.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListDocumentBlockRequest = ListDocumentBlockRequest.builder() \
        .document_id("doxcnePuYufKa49ISjhD8Ih0ikh") \
        .page_size(500) \
        .page_token(
        "aw7DoMKBFMOGwqHCrcO8w6jCmMOvw6ILeADCvsKNw57Di8O5XGV3LG4_w5HCqhFxSnDCrCzCn0BgZcOYUg85EMOYcEAcwqYOw4ojw5QFwofCu8KoIMO3K8Ktw4IuNMOBBHNYw4bCgCV3U1zDu8K-J8KSR8Kgw7Y0fsKZdsKvW3d9w53DnkHDrcO5bDkYwrvDisOEPcOtVFJ-I03CnsOILMOoAmLDknd6dsKqG1bClAjDuS3CvcOTwo7Dg8OrwovDsRdqIcKxw5HDohTDtXN9w5rCkWo") \
        .document_revision_id(-1) \
        .user_id_type("user_id") \
        .build()

    # 发起请求
    response: ListDocumentBlockResponse = client.docx.v1.document_block.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.docx.v1.document_block.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
