from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session

from app.core.logger import get_logger
from app.db.database import get_db
from app.models.input.score_input import ScoreInput
from app.models.output.score_output import ScoreOutput
from app.models.output.upload_response import UploadResponse
from app.services.score_service import calculate_score
from app.services.status_service import get_job_status
from app.services.upload_service import process_csv_upload

logger = get_logger(__name__)
router = APIRouter()


@router.post("/submit-score", response_model=ScoreOutput)
def submit_score(data: ScoreInput, db: Session = Depends(get_db)):
    logger.info("POST /submit-score called")
    result = calculate_score(data, db)  # precisa ajustar o service para aceitar `db`
    return result


@router.post("/upload-csv", response_model=UploadResponse)
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    logger.info("POST /upload-csv called")
    return await process_csv_upload(file, db)  # idem aqui


@router.get("/credit-score/{job_id}")
def check_credit_score_status(job_id: str, db: Session = Depends(get_db)):
    return get_job_status(job_id, db)  # idem aqui
