from fastapi import FastAPI
from app.api.routes import router
from app.core.logger import get_logger
from app.services.worker import worker_loop
import asyncio

logger = get_logger(__name__)

app = FastAPI(title="Lucas Quality AI Portfolio")

logger.info("Starting FastAPI application")

app.include_router(router)

@app.on_event("startup")
async def start_worker():
    logger.info("Starting worker loop...")
    asyncio.create_task(worker_loop())
