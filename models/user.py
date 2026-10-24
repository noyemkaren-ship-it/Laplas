from sqlalchemy import Column, String, Integer, Boolean
from base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, unique=True, nullable=False)
    num = Column(String)
    age = Column(Integer)
    password = Column(String, nullable=False)
    admin = Column(Boolean, default=False)
    xp = Column(Integer, default=0)