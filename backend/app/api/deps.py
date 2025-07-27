from typing import Generator, Optional
from app.db.session import SessionLocal
from fastapi import Depends, HTTPException, status
from app.core.auth import oauth2_scheme, oauth2_scheme_force
from app.core.auth import decode_access_token
from app.schemas.user import UserToken


def get_db() -> Generator:
    db = SessionLocal()
    db.current_user_id = None
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme)) -> Optional[UserToken]:
    decoded_token = decode_access_token(token)
    if decoded_token is not None:
        current_user = UserToken(**decoded_token)
        return current_user
    return None

def require_user(token: str = Depends(oauth2_scheme_force)) -> UserToken:
    current_user = get_current_user(token)
    if current_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return current_user

def require_admin(token: str = Depends(oauth2_scheme_force)) -> UserToken:
    current_user = require_user(token)
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )
    return current_user
