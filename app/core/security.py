from passlib.context import CryptContext

PWD_CONTEXT = CryptContext(schemes=["argon2"], default="argon2", deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return PWD_CONTEXT.hash(password)
