from typing import Optional
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from app.core.config import settings
import logging

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}{settings.AUTH_PREFIX}{settings.TOKEN_ENDPOINT}", auto_error=False)
oauth2_scheme_force = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}{settings.AUTH_PREFIX}{settings.TOKEN_ENDPOINT}")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM])
        return payload
    except Exception as error:
        logging.warning(str(error))
        return None
