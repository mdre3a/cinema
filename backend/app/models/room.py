from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Room(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    max_rows = Column(Integer, nullable=False)
    max_seats = Column(Integer, nullable=False)
    schedules = relationship("Schedule", back_populates="room", uselist=True)
