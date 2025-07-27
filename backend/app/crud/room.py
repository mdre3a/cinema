from typing import Any, Optional, Type
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase, ModelType
from app.models.room import Room
from app.models.schedule import Schedule
from app.schemas.room import RoomCreate, RoomUpdate


class CRUDRoom(CRUDBase[Room, RoomCreate, RoomUpdate]):
    def get_rooms(
            self, db: Session, *, room_id: int = None, movie_id: int = None, skip: int = 0,
            limit: int = 100
    ) -> list[Type[ModelType]]:
        filters = []
        if room_id is not None:
            filters.append(Schedule.room_id == room_id)
        if movie_id is not None:
            filters.append(Schedule.movie_id == movie_id)
        if len(filters) < 1:
            filters = None
        query = db.query(Room).join(Room.schedules)
        if filters:
            for condition in filters:
                query = query.filter(condition)
        return query.offset(skip).limit(limit).all()

    def get_by_schedule_id(self, db: Session, id: Any) -> Optional[Room]:
        return db.query(Room).join(Room.schedules).filter(Schedule.id == id).first()


room = CRUDRoom(Room)
