from fastapi import APIRouter, UploadFile, File

from app.models.input.score_input import ScoreInput
from app.models.output.score_output import ScoreOutput
from app.models.output.upload_response import UploadResponse

from app.services.score_service import calculate_score
from app.services.upload_service import process_csv_upload
from app.services.status_service import get_job_status

from app.core.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()

@router.post("/submit-score", response_model=ScoreOutput)
def submit_score(data: ScoreInput):
    logger.info("POST /submit-score called")
    result = calculate_score(data)
    return result

@router.post("/upload-csv", response_model=UploadResponse)
async def upload_csv(file: UploadFile = File(...)):
    logger.info("POST /upload-csv called")
    return await process_csv_upload(file)

@router.get("/credit-score/{job_id}")
def check_credit_score_status(job_id: str):
    return get_job_status(job_id)