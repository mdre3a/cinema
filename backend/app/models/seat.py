from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Seat(Base):
    id = Column(Integer, primary_key=True, index=True)
    row = Column(Integer, server_default=None, nullable=False)
    seat = Column(Integer, server_default=None, nullable=False)
    schedule_id = Column(Integer, ForeignKey('schedule.id', name="fk_seat_schedule_id", ondelete='CASCADE', onupdate='RESTRICT'), nullable=False)
    schedule = relationship(
        "Schedule",
        # cascade="all",
        back_populates="seats",
        uselist=False,
    )
    user_id = Column(Integer, ForeignKey('user.id', name="fk_seat_user_id", ondelete='CASCADE', onupdate='RESTRICT'), nullable=False)
    user = relationship(
        "User",
        # cascade="all",
        back_populates="seats",
        uselist=False,
    )

    __table_args__ = (
        UniqueConstraint('row', 'seat', 'schedule_id', name='uq_row_seat_schedule'),
    )
