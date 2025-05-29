import time

from app.core.logger import get_logger
from app.models.input.score_input import ScoreInput
from app.repositories.factory import get_repository
from app.services import score_service

logger = get_logger(__name__)


def _process_job(repository, job):
    logger.info(f"Processing job_id={job.job_id}")
    inputs = repository.get_inputs(job.job_id)

    if not inputs:
        logger.warning(f"No inputs found for job_id={job.job_id}")
        repository.update_job_status(job.job_id, "error")
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
            repository.save_output(job.job_id, score_output)
        except Exception as e:
            logger.error(f"Error processing input_id={input_record.id}: {e}")
            repository.update_job_status(job.job_id, "error")
            return

    repository.update_job_status(job.job_id, "completed")
    logger.info(f"Job job_id={job.job_id} completed")


def process_pending_jobs(polling_interval: int = 10):
    while True:
        repository = get_repository()
        try:
            pending_jobs = repository.get_pending_jobs()
            if not pending_jobs:
                logger.info("No pending jobs found. Sleeping...")
            for job in pending_jobs:
                _process_job(repository, job)
        except Exception as e:
            import traceback

            print("TRACEBACK:\n", traceback.format_exc())
        time.sleep(polling_interval)
