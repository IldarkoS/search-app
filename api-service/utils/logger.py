import os
import sys

from loguru import logger

logger.remove()

if os.getenv("ENV") == "production":
    logger.add(sys.stdout, level="INFO", serialize=True)
else:
    logger.add(
        sys.stdout,
        level="DEBUG",
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
               "<level>{level: <8}</level> | "
               "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
               "<level>{message}</level>",
        backtrace=True,
        diagnose=True
    )
