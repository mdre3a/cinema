from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    email = Column(String(255), index=True, nullable=False, unique=True)
    hashed_password = Column(String(255), index=True, nullable=False)
    role = Column(String(10), default="user", nullable=False)
    seats = relationship("Seat", back_populates="user", uselist=True)
