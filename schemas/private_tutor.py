from pydantic import BaseModel

class PrivateTutorSchema(BaseModel):
    name: str
    subject: str
    description: str
    initials: str