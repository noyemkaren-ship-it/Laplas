from pydantic import BaseModel

class TestSchema(BaseModel):
    subject: str
    question: str
    answer: str

class TestOut(BaseModel):
    subject: str
    question: str

class Answer(BaseModel):
    test_id: int
    answer: str