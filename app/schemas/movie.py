from __future__ import annotations
from typing import Optional, Sequence, List, TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemas.schedule import Schedule, ScheduleRoom


class MovieBase(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


class MovieCreate(MovieBase):
    name: str


class MovieUpdate(MovieBase):
    name: str


class MoviePosterUpdate(MovieBase):
    poster: Optional[str]


class MovieInDB(MovieBase):
    id: int
    name: str
    poster: Optional[str]


class Movie(MovieInDB):
    pass


class MovieShowtime(MovieInDB):
    schedules: List['ScheduleRoom']


class MovieSearchResults(BaseModel):
    results: Sequence[Movie]
