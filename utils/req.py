from datetime import datetime, timedelta, timezone
import jwt
from fastapi import Request, Response

SECRET_KEY = "X4R-0ui9VN6x1TXPaWMw7-icJeLfozHcGOT7XRPqZkszQLPjycycNeNICqrZQEeg"
ALGORITHM = "HS256"
COOKIE_KEY = "data"
COOKIE_MAX_AGE = 60 * 60 * 24 * 7  # 7 дней


def _encode_id(user_id: int) -> str:
    payload = {
        "sub": str(user_id),
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(seconds=COOKIE_MAX_AGE),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def _decode_id(token: str) -> int | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return int(payload["sub"])
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, KeyError, ValueError):
        return None


def get_id(request: Request) -> int | None:
    token = request.cookies.get(COOKIE_KEY)
    if not token:
        return None
    return _decode_id(token)


def create_cookie(response: Response, user_id: int) -> None:
    token = _encode_id(user_id)
    response.set_cookie(
        key=COOKIE_KEY,
        value=token,
        max_age=COOKIE_MAX_AGE,
        httponly=True,
        samesite="lax",       # ← было "none" — на HTTP браузер выкидывал cookie
        secure=False,         # ← явно False для локальной разработки
        path="/",
    )


def delete_cookie(response: Response) -> None:
    response.delete_cookie(
        key=COOKIE_KEY,
        path="/",
        httponly=True,
        samesite="lax",
        secure=False,
    )