# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .combined_job_result_default_job_post import CombinedJobResultDefaultJobPost
from .job import Job
from .job_manager import JobManager
from .registration_schema_info import RegistrationSchemaInfo


class CombinedJobResult(object):
    _types = {
        "default_job_post": CombinedJobResultDefaultJobPost,
        "job": Job,
        "job_manager": JobManager,
        "interview_registration_schema_info": RegistrationSchemaInfo,
        "onboard_registration_schema_info": RegistrationSchemaInfo,
    }

    def __init__(self, d):
        self.default_job_post: Optional[CombinedJobResultDefaultJobPost] = None
        self.job: Optional[Job] = None
        self.job_manager: Optional[JobManager] = None
        self.interview_registration_schema_info: Optional[RegistrationSchemaInfo] = None
        self.onboard_registration_schema_info: Optional[RegistrationSchemaInfo] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CombinedJobResultBuilder":
        return CombinedJobResultBuilder()


class CombinedJobResultBuilder(object):
    def __init__(self, combined_job_result: CombinedJobResult = CombinedJobResult({})) -> None:
        self._combined_job_result: CombinedJobResult = combined_job_result

    def default_job_post(self, default_job_post: CombinedJobResultDefaultJobPost) -> "CombinedJobResultBuilder":
        self._combined_job_result.default_job_post = default_job_post
        return self

    def job(self, job: Job) -> "CombinedJobResultBuilder":
        self._combined_job_result.job = job
        return self

    def job_manager(self, job_manager: JobManager) -> "CombinedJobResultBuilder":
        self._combined_job_result.job_manager = job_manager
        return self

    def interview_registration_schema_info(self,
                                           interview_registration_schema_info: RegistrationSchemaInfo) -> "CombinedJobResultBuilder":
        self._combined_job_result.interview_registration_schema_info = interview_registration_schema_info
        return self

    def onboard_registration_schema_info(self,
                                         onboard_registration_schema_info: RegistrationSchemaInfo) -> "CombinedJobResultBuilder":
        self._combined_job_result.onboard_registration_schema_info = onboard_registration_schema_info
        return self

    def build(self) -> "CombinedJobResult":
        return self._combined_job_result
