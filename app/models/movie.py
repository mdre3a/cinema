from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Movie(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    poster = Column(String(255), index=True, nullable=True)
    schedules = relationship("Schedule", back_populates="movie", uselist=True)
