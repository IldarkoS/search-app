import traceback
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from lib.logger import logger


class ExceptionLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        try:
            response = await call_next(request)
            return response
        except Exception as exc:
            tb = traceback.format_exc()

            logger.exception(
                f"Unhandled error at {request.method} {request.url.path} | request_id={request_id}\n{tb}"
            )

            return JSONResponse(
                status_code=500,
                content={
                    "error": "Internal Server Error",
                    "request_id": request_id
                }
            )
