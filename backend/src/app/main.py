import structlog
from fastapi import FastAPI

from app.config.logging import configure_logging
from app.config.settings import settings


configure_logging()

logger = structlog.get_logger()

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health() -> dict[str, str]:
    logger.info("health_check")
    return {"status": "ok"}