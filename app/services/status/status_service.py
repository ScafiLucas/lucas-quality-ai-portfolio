from app.core.job_tracker import JobStatus, job_result_map, job_status_map


def get_job_status(job_id: str) -> dict:
    status = job_status_map.get(job_id)
    if status is None:
        return {"status": "not_found"}

    if status == JobStatus.DONE:
        return {"status": "done", "results": job_result_map[job_id]}

    return {"status": status}
