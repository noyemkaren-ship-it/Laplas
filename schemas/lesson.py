from pydantic import BaseModel

class Lesson(BaseModel):
    name: str
    subject: str
    num: int
    lesson_html: str
    lesson_type: str


class LessonOut(BaseModel):
    name: str
    subject: str
    num: int