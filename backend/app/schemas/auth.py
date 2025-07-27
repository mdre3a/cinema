from typing import Optional, Sequence
from pydantic import BaseModel, EmailStr
from .user import User

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: Optional[int] = None  # in seconds, optional
    refresh_token: Optional[str] = None
    user: Optional[User] = None

class TokenData(BaseModel):
    username: Optional[str] = None
    is_admin: Optional[bool] = False