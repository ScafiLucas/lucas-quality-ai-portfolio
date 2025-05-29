import time
from sqlalchemy.orm import Session
from app.core.logger import logger
from app.db.database import SessionLocal
from app.services import db_service, score_service
from app.models.input.score_input import ScoreInput


def _get_pending_jobs(db: Session):
    return db_service.get_pending_jobs(db)


def _process_job(db: Session, job):
    logger.info(f"Processing job_id={job.job_id}")

    inputs = db_service.get_inputs_by_job_id(db, job.job_id)

    if not inputs:
        logger.warning(f"No inputs found for job_id={job.job_id}")
        db_service.update_job_status(db, job.job_id, "error")
        return

    for input_record in inputs:
        try:
            score_input = ScoreInput(
                income=input_record.income,
                debt=input_record.debt,
                late_payments=input_record.late_payments,
                savings=input_record.savings,
            )
            score_output = score_service.calculate_score(score_input)
            db_service.persist_score_result(db, score_output, job.job_id)
        except Exception as e:
            logger.error(f"Error processing input_id={input_record.id}: {e}")
            db_service.update_job_status(db, job.job_id, "error")
            return

    db_service.update_job_status(db, job.job_id, "completed")
    logger.info(f"Job job_id={job.job_id} completed")


def process_pending_jobs(polling_interval: int = 10):
    while True:
        db = SessionLocal()
        try:
            pending_jobs = _get_pending_jobs(db)
            if not pending_jobs:
                logger.info("No pending jobs found. Sleeping...")
            for job in pending_jobs:
                _process_job(db, job)
        except Exception as e:
            logger.exception(f"Worker loop failed: {e}")
        finally:
            db.close()
        time.sleep(polling_interval)
