from datetime import datetime

from alembic import op, context
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.movie import Movie
from app.models.room import Room
from app.models.schedule import Schedule
from app.core.security import get_password_hash


def upgrade() -> None:
    """Upgrade schema."""
    if not context.is_offline_mode():
        bind = op.get_bind()
        session = Session(bind=bind)
        # noinspection PyArgumentList
        admin_user = User(id=1, email='admin@localdemo.com', hashed_password=get_password_hash("123"), name="Administrator", role="admin")
        # noinspection PyArgumentList
        typical_user = User(id=2, email='user@localdemo.com', hashed_password=get_password_hash("123"), name="User", role="user")
        _id = 0
        movies = [
            Movie(id=(_id := _id + 1), name="The Shawshank Redemption"),
            Movie(id=(_id := _id + 1), name="The Godfather"),
            Movie(id=(_id := _id + 1), name="The Dark Knight"),
            Movie(id=(_id := _id + 1), name="12 Angry Men"),
            Movie(id=(_id := _id + 1), name="The Lord of the Rings: The Return of the King"),
            Movie(id=(_id := _id + 1), name="Schindler's List"),
            Movie(id=(_id := _id + 1), name="Pulp Fiction")
        ]
        _id = 0
        rooms = [
            Room(id=(_id := _id + 1), name='Red', max_rows=10, max_seats=8),
            Room(id=(_id := _id + 1), name='Green', max_rows=10, max_seats=8),
            Room(id=(_id := _id + 1), name='Blue', max_rows=10, max_seats=8)
        ]
        _id = 0
        date_format = "%Y-%m-%d %H:%M:%S"
        schedules = [
            Schedule(id=(_id := _id + 1), show_time=datetime.strptime("2025-07-01 12:00:00", date_format), movie_id=4, room_id=1),
            Schedule(id=(_id := _id + 1), show_time=datetime.strptime("2025-07-01 14:00:00", date_format), movie_id=6, room_id=1),
            Schedule(id=(_id := _id + 1), show_time=datetime.strptime("2025-07-01 16:30:00", date_format), movie_id=5, room_id=1),
            Schedule(id=(_id := _id + 1), show_time=datetime.strptime("2025-07-01 19:00:00", date_format), movie_id=4, room_id=1),

            Schedule(id=(_id := _id + 1), show_time=datetime.strptime("2025-07-01 12:00:00", date_format), movie_id=6, room_id=2),
            Schedule(id=(_id := _id + 1), show_time=datetime.strptime("2025-07-01 14:00:00", date_format), movie_id=2, room_id=2),
            Schedule(id=(_id := _id + 1), show_time=datetime.strptime("2025-07-01 16:30:00", date_format), movie_id=5, room_id=2),
            Schedule(id=(_id := _id + 1), show_time=datetime.strptime("2025-07-01 19:00:00", date_format), movie_id=4, room_id=2),

            Schedule(id=(_id := _id + 1), show_time=datetime.strptime("2025-07-01 12:00:00", date_format), movie_id=7, room_id=3),
            Schedule(id=(_id := _id + 1), show_time=datetime.strptime("2025-07-01 14:00:00", date_format), movie_id=2, room_id=3),
            Schedule(id=(_id := _id + 1), show_time=datetime.strptime("2025-07-01 16:30:00", date_format), movie_id=1, room_id=3),
            Schedule(id=(_id := _id + 1), show_time=datetime.strptime("2025-07-01 19:00:00", date_format), movie_id=4, room_id=3),

        ]
        session.bulk_save_objects([admin_user, typical_user])
        session.bulk_save_objects(rooms)
        session.bulk_save_objects(movies)
        session.bulk_save_objects(schedules)
        session.commit()
        """Upgrade schema."""


def downgrade() -> None:
    """Downgrade schema."""
    pass
