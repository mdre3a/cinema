from sqlalchemy.orm.session import Session
from app.models.room import Room


def update(db: Session):
    _id = 0
    rooms = [
        Room(id=(_id := _id + 1), name='Red', max_rows=10, max_seats=8),
        Room(id=(_id := _id + 1), name='Green', max_rows=10, max_seats=8),
        Room(id=(_id := _id + 1), name='Blue', max_rows=10, max_seats=8)
    ]
    db.bulk_save_objects(rooms)
