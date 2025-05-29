from pydantic import BaseModel
from typing import Optional

class UploadResponse(BaseModel):
    filename: str
    status: str
    message: str
    job_id: Optional[str] = None