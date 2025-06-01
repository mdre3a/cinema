from typing import Optional, Sequence
from pydantic import BaseModel, EmailStr


class RoomBase(BaseModel):
    name: str
    max_rows: int
    max_seats: int


class RoomCreate(RoomBase):
    pass


class RoomUpdate(RoomBase):
    pass


class RoomInDB(RoomBase):
    id: int
    name: str


class Room(RoomInDB):
    class Config:
        orm_mode = True


class RoomSearchResults(BaseModel):
    results: Sequence[Room]
