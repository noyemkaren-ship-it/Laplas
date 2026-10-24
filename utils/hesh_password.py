from argon2 import PasswordHasher
from argon2.exceptions import VerificationError

_ph = PasswordHasher()

def hash_psw(password: str) -> str:
    return _ph.hash(password)

def verify_psw(password: str, hashed: str | None) -> bool:
    if not hashed:
        return False
    try:
        return _ph.verify(hashed, password)
    except VerificationError:
        return False