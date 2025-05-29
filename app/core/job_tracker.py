from typing import Dict
from enum import Enum

class JobStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    DONE = "done"
    ERROR = "error"

job_status_map: Dict[str, JobStatus] = {}
job_result_map: Dict[str, dict] = {}
