import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from utils.logger import logger


class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        method = request.method
        path = request.url.path
        user_agent = request.headers.get("user-agent", "-")

        start_time = time.time()
        response = await call_next(request)
        duration = round((time.time() - start_time) * 1000, 2)

        logger.info(
            f"{method} {path} | {response.status_code} | {duration}ms | {user_agent} | request_id={request_id}"
        )

        response.headers["X-Request-ID"] = request_id
        return response
