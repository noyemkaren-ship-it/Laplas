from pydantic import BaseModel

class CompletedSchema(BaseModel):
    lesson_id: int
