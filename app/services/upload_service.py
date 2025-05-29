import os
import csv
import uuid
from fastapi import UploadFile
from app.models.output.upload_response import UploadResponse
from app.core.job_queue import job_queue
from app.core.job_tracker import job_status_map, JobStatus
from app.core.logger import get_logger

REQUIRED_COLUMNS = {"income", "debt", "late_payments", "savings"}
logger = get_logger(__name__)

async def process_csv_upload(file: UploadFile) -> UploadResponse:
    logger.info("Received file upload", extra={"uploaded_filename": file.filename})

    try:
        contents = await file.read()
        decoded = contents.decode("utf-8").splitlines()
        reader = csv.DictReader(decoded)

        if not REQUIRED_COLUMNS.issubset(reader.fieldnames or []):
            missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
            logger.warning(
                "CSV missing required columns",
                extra={"uploaded_filename": file.filename, "missing_columns": list(missing)}
            )
            return UploadResponse(
                filename=file.filename,
                status="error",
                message=f"CSV missing required columns: {missing}"
            )

        os.makedirs("temp", exist_ok=True)
        filepath = f"temp/{file.filename}"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(decoded) + "\n")

        logger.info("CSV file validated and saved", extra={"uploaded_filename": file.filename})

        job_id = str(uuid.uuid4())
        job_status_map[job_id] = JobStatus.PENDING
        await job_queue.put({"job_id": job_id, "filepath": filepath})

        logger.info("Job enqueued for processing", extra={"job_id": job_id, "uploaded_filename": file.filename})

        return UploadResponse(
            filename=file.filename,
            status="success",
            message=f"File enqueued for processing. Job ID: {job_id}",
            job_id=job_id
        )

    except Exception as e:
        logger.error(
            "Failed to process file",
            extra={"uploaded_filename": file.filename, "error": str(e)}
        )
        return UploadResponse(
            filename=file.filename,
            status="error",
            message=f"Failed to process file: {str(e)}"
        )
