# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.sheets.v3 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ReplaceSpreadsheetSheetRequest = ReplaceSpreadsheetSheetRequest.builder() \
        .spreadsheet_token("shtcnmBA*****yGehy8") \
        .sheet_id("0b**12") \
        .request_body(Replace.builder()
                      .find_condition(FindCondition.builder().build())
                      .find("str")
                      .replacement("str")
                      .build()) \
        .build()

    # 发起请求
    response: ReplaceSpreadsheetSheetResponse = client.sheets.v3.spreadsheet_sheet.replace(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.sheets.v3.spreadsheet_sheet.replace failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
