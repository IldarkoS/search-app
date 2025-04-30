import logging
import sys
from contextvars import ContextVar

import structlog


_request_logger: ContextVar[structlog.BoundLogger] = ContextVar("request_logger", default=None)

def init_logger(log_level: str = "INFO") -> None:
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, log_level.upper(), logging.INFO),
    )

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.stdlib.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

def get_logger() -> structlog.BoundLogger:
    logger = _request_logger.get()
    if logger is None:
        return structlog.get_logger()
    return logger

def bind_request_logger(**kwargs) -> None:
    logger = structlog.get_logger().bind(**kwargs)
    _request_logger.set(logger)
