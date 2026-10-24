from base import Base
from sqlalchemy import Integer, Column

class Completed(Base):
    __tablename__ = "completeds"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    lesson_id = Column(Integer, nullable=False)