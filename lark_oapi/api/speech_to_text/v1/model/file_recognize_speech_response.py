# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .file_recognize_speech_response_body import FileRecognizeSpeechResponseBody


class FileRecognizeSpeechResponse(BaseResponse):
    _types = {
        "data": FileRecognizeSpeechResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[FileRecognizeSpeechResponseBody] = None
        init(self, d, self._types)
