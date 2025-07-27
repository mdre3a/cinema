from sqlalchemy.orm.session import Session

from app.api.v1 import schedule
from app.models.seat import Seat
from datetime import datetime


def update(db: Session):
    date_format = "%Y-%m-%d %H:%M:%S"
    _id = 0
    seats = [
        Seat(id=(_id := _id + 1), row=1, seat=1, schedule_id=1, user_id=2),
    ]
    db.bulk_save_objects(seats)
