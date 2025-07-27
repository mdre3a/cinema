from sqlalchemy.orm.session import Session
from app.db.session import SessionLocal
import mock.movie as movie
import mock.room as room
import mock.schedule as schedule
import mock.seat as seat
import mock.user as user
import app.models


def main():
    db = SessionLocal()

    user.update(db=db)
    room.update(db=db)
    movie.update(db=db)
    schedule.update(db=db)
    seat.update(db=db)
    db.commit()

if __name__ == "__main__":
    main()