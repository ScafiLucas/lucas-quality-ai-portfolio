import asyncio
import csv
import uuid
from app.core.job_queue import job_queue
from app.core.job_tracker import job_status_map, job_result_map, JobStatus
from app.services.score_service import calculate_score
from app.models.input.score_input import ScoreInput
from app.core.logger import get_logger

logger = get_logger(__name__)

async def worker_loop():
    while True:
        job = await job_queue.get()
        job_id = job["job_id"]
        filepath = job["filepath"]

        logger.info("Worker started job", extra={"job_id": job_id, "filepath": filepath})
        job_status_map[job_id] = JobStatus.PROCESSING

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                results = []

                logger.info("Starting CSV row processing", extra={"job_id": job_id})
                for row in reader:
                    logger.info("Processing row", extra={"row_data": row})
                    input_data = ScoreInput(
                        income=float(row["income"]),
                        debt=float(row["debt"]),
                        late_payments=int(row["late_payments"]),
                        savings=float(row["savings"])
                    )
                    result = calculate_score(input_data)
                    results.append(result.dict())
                    logger.info("Score calculated", extra={"job_id": job_id, "score": result.score})
                    logger.debug("Score result details", extra={"job_id": job_id, "output": result.dict()})
    
                job_result_map[job_id] = results
                job_status_map[job_id] = JobStatus.DONE
                logger.info("Worker finished job", extra={"job_id": job_id, "entries": len(results)})

        except Exception as e:
            job_status_map[job_id] = JobStatus.ERROR
            logger.error("Worker failed job", extra={"job_id": job_id, "error": str(e)})

        job_queue.task_done()
