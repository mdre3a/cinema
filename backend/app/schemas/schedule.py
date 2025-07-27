from __future__ import annotations
from datetime import datetime
from typing import Sequence, TYPE_CHECKING
from pydantic import BaseModel

from app.schemas.room import Room

if TYPE_CHECKING:
    from app.schemas.movie import Movie, MovieShowtime


class ScheduleBase(BaseModel):
    show_time: datetime
    room_id: int
    movie_id: int

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


class ScheduleCreate(ScheduleBase):
    pass


class ScheduleUpdate(ScheduleBase):
    pass


class ScheduleRoom(ScheduleBase):
    id: int
    movie_id: int
    room_id: int
    room: Room


class ScheduleInDB(ScheduleRoom):
    movie: 'Movie'


class Schedule(ScheduleInDB):
    pass


class ScheduleSearchResults(BaseModel):
    results: Sequence[Schedule]
