from typing import Type
from sqlalchemy.orm import Session, joinedload
from app.crud.base import CRUDBase, ModelType
from app.models import Schedule
from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieUpdate


class CRUDMovie(CRUDBase[Movie, MovieCreate, MovieUpdate]):
    def get_movies(
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
        query = db.query(Movie).join(Movie.schedules).options(joinedload(Movie.schedules))
        if filters:
            for condition in filters:
                query = query.filter(condition)
        return query.offset(skip).limit(limit).all()


movie = CRUDMovie(Movie)
