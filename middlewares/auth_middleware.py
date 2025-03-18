from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from core.security import verify_token


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/protected"):
            token = request.headers.get("Authorization")
            if token is None or not verify_token(token):
                return Response("Unauthorized", status_code=401)
        response = await call_next(request)
        return response