from base import Base
from sqlalchemy import Column, Integer, String

class Test(Base):
    __tablename__ = "tests"
    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)