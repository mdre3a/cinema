from typing import Optional
from pydantic import BaseModel
from .schedule import Schedule


class SeatBase(BaseModel):
    row: int
    seat: int

    class Config:
        orm_mode = True


class SeatCreate(SeatBase):
    schedule_id: int
    user_id: int


class SeatUpdate(SeatBase):
    pass


class SeatInDB(SeatBase):
    id: int
    schedule_id: int
    schedule: Schedule
    user_id: int


class Seat(SeatInDB):
    user_id: Optional[int]
