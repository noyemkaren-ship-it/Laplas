from sqlalchemy import Column, Integer, String
from base import Base

class Lesson(Base):
    """
        Модель для Lesson,
        type lesson это тип урока,
        он может быть, как и test
        и тогда урок отобразиться как тест,
        Видов уроков будет не мало.
    """
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    num = Column(Integer, nullable=False)
    lesson_html = Column(String, nullable=False)
    lesson_type = Column(String, nullable=False)
