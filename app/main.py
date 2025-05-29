import asyncio

from fastapi import FastAPI

from app.api.routes import router
from app.core.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(title="Lucas Quality AI Portfolio")

logger.info("Starting FastAPI application")

app.include_router(router)
