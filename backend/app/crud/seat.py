from typing import Type
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase, ModelType
from app.models import Schedule
from app.models.seat import Seat
from app.schemas.seat import SeatCreate, SeatUpdate


class CRUDSeat(CRUDBase[Seat, SeatCreate, SeatUpdate]):
    def get_reserved_seats(
            self, db: Session, *, room_id: int = None, schedule_id: int = None, movie_id: int = None, user_id: int = None, skip: int = 0,
            limit: int = 100
    ) -> list[Type[ModelType]]:
        filters = []
        if room_id is not None:
            filters.append(Schedule.room_id == room_id)
        if schedule_id is not None:
            filters.append(Seat.schedule_id == schedule_id)
        if user_id is not None:
            filters.append(Seat.user_id == user_id)
        if movie_id is not None:
            filters.append(Schedule.movie_id == movie_id)
        if len(filters) < 1:
            filters = None
        query = db.query(Seat).join(Seat.schedule)
        if filters:
            for condition in filters:
                query = query.filter(condition)
        return query.offset(skip).limit(limit).all()


seat = CRUDSeat(Seat)
