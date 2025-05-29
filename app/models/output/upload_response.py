from typing import Optional

from pydantic import BaseModel


class UploadResponse(BaseModel):
    filename: str
    status: str
    message: str
    job_id: Optional[str] = None
