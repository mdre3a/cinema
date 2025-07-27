from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr] = None
    role: str

    class Config:
        orm_mode = True


class UserToken(UserBase):
    id: int
    pass


class UserCreate(UserBase):
    email: EmailStr


class UserUpdate(UserBase):
    ...


class UserInDBBase(UserBase):
    id: Optional[int] = None


class User(UserInDBBase):
    pass
