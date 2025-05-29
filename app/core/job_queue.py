import asyncio

job_queue = asyncio.Queue()


def enqueue_job(job_data: dict):
    job_queue.put_nowait(job_data)
