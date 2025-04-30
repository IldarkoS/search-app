import os
import sys

from loguru import logger

from config import settings

logger.remove()

if os.getenv("ENV") == "production":
    logger.add(sys.stdout, level="INFO", serialize=True)
else:
    logger.add(
        sys.stdout,
        level=settings.log_level.upper(),
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
               "<level>{level: <8}</level> | "
               "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
               "<level>{message}</level>",
        enqueue=True,
        backtrace=True,
        diagnose=True
    )

    logger.info("Logger initialized with level: {}", settings.log_level.upper())
