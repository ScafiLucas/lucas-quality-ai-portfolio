import uuid
from enum import Enum
from typing import Dict


class JobStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    DONE = "done"
    ERROR = "error"


job_status_map: Dict[str, JobStatus] = {}
job_result_map: Dict[str, dict] = {}


def create_job_id() -> str:
    return str(uuid.uuid4())


class JobStatusTracker:
    @staticmethod
    def set_status(job_id: str, status: JobStatus):
        job_status_map[job_id] = status

    @staticmethod
    def get_status(job_id: str) -> JobStatus:
        return job_status_map.get(job_id, JobStatus.PENDING)

    @staticmethod
    def set_result(job_id: str, result: dict):
        job_result_map[job_id] = result

    @staticmethod
    def get_result(job_id: str) -> dict:
        return job_result_map.get(job_id, {})
