from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from base import Base


class PrivateTutor(Base):
    __tablename__ = 'private_tutors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    description = Column(String, nullable=False)
    initials = Column(String, nullable=False)