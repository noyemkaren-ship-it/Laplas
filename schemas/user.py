from pydantic import BaseModel, ConfigDict, field_validator


class UserIn(BaseModel):
    name: str
    email: str
    num: str
    age: int
    password: str

    @field_validator("age")
    @classmethod
    def check_age(cls, value):
        if value < 0:
            raise ValueError("age must be >= 0")
        elif value > 80:
            raise ValueError("age must be <= 80")
        return value


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
    num: str
    age: int
    xp: int
    admin: bool


class UserLogin(BaseModel):
    email: str
    password: str