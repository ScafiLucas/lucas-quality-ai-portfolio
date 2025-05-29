import csv
import io
import logging
from typing import List

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.core.job_queue import enqueue_job
from app.core.job_tracker import JobStatusTracker, create_job_id
from app.models.input.score_input import ScoreInput
from app.models.output.upload_response import UploadResponse
from app.repositories.factory import get_repository

logger = logging.getLogger(__name__)


def process_csv_upload(file: UploadFile, db: Session) -> UploadResponse:
    job_id = create_job_id()
    tracker = JobStatusTracker(db)
    tracker.register_job(job_id)

    rows = _parse_csv(file)
    score_inputs = _transform_rows(rows)
    _persist_inputs(score_inputs, job_id, db)
    _enqueue_processing(job_id)

    return UploadResponse(
        job_id=job_id,
        status="processing",
        detail=f"Successfully received {len(score_inputs)} records.",
    )


def _parse_csv(file: UploadFile) -> List[dict]:
    try:
        try:
            content = file.file.read().decode("utf-8")
        except UnicodeDecodeError:
            file.file.seek(0)
            content = file.file.read().decode("latin-1")
        reader = csv.DictReader(io.StringIO(content))
        return list(reader)
    except Exception as e:
        logger.exception("Failed to read or parse CSV file.")
        raise ValueError("Invalid CSV file") from e


def _transform_rows(rows: List[dict]) -> List[ScoreInput]:
    valid_inputs = []
    for row in rows:
        try:
            score_input = ScoreInput(
                income=float(row["income"]),
                debt=float(row["debt"]),
                savings=float(row["savings"]),
                late_payments=int(row["late_payments"]),
            )
            valid_inputs.append(score_input)
        except Exception as e:
            logger.warning(f"Invalid row skipped: {row} – {e}")
    return valid_inputs


def _persist_inputs(inputs: List[ScoreInput], job_id: str, db: Session) -> None:
    for score_input in inputs:
        try:
            repository = get_repository()
            repository.save_input(job_id, score_input)
        except Exception as e:
            logger.warning(f"Failed to persist input: {score_input} – {e}")


def _enqueue_processing(job_id: str) -> None:
    try:
        enqueue_job(job_id)
    except Exception as e:
        logger.error(f"Failed to enqueue job {job_id}: {e}")
        raise
