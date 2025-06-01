from sqlalchemy import Column, Integer,  DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Schedule(Base):
    id = Column(Integer, primary_key=True, index=True)
    show_time = Column(DateTime, server_default=None, nullable=False)
    movie_id = Column(Integer, ForeignKey('movie.id', name="fk_schedule_movie_id", ondelete='CASCADE', onupdate='RESTRICT'), nullable=False)
    movie = relationship(
        "Movie",
        # cascade="all",
        back_populates="schedules",
        uselist=False,
    )
    room_id = Column(Integer, ForeignKey('room.id', name="fk_schedule_room_id", ondelete='CASCADE', onupdate='RESTRICT'), nullable=False)
    room = relationship(
        "Room",
        # cascade="all",
        back_populates="schedules",
        uselist=False,
    )

    seats = relationship("Seat", back_populates="schedule", uselist=True)

    __table_args__ = (
        UniqueConstraint('show_time', 'room_id', name='uq_show_time_room'),
    )
