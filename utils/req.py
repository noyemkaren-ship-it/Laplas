from datetime import datetime, timedelta, timezone
import jwt
from fastapi import Request, Response

SECRET_KEY = "X4R-0ui9VN6x1TXPaWMw7-icJeLfozHcGOT7XRPqZkszQLPjycycNeNICqrZQEeg"
ALGORITHM = "HS256"
COOKIE_KEY = "data"
COOKIE_MAX_AGE = 60 * 60 * 24 * 7  # 7 дней


def _encode_id(user_id: int) -> str:
    """Шифрует (подписывает) id в JWT-токен."""
    payload = {
        "sub": str(user_id),
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + timedelta(seconds=COOKIE_MAX_AGE),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def _decode_id(token: str) -> int | None:
    """Расшифровывает (проверяет) JWT-токен и возвращает id или None."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return int(payload["sub"])
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, KeyError, ValueError):
        return None


def get_id(request: Request) -> int | None:
    """Функция для получения id с помощью файлов cookie."""
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
        samesite="none",
        path="/",
    )


def delete_cookie(response: Response) -> None:
    """Удаляет cookie с id."""
    response.delete_cookie(key=COOKIE_KEY, path="/")