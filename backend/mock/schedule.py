from sqlalchemy.orm.session import Session
from app.models.schedule import Schedule
from datetime import datetime


def update(db: Session):
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
    db.bulk_save_objects(schedules)