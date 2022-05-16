from datetime import datetime
from pydantic import BaseModel, EmailStr, SecretStr

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    name: str
    # age: int
    # gender: str

    # zip_code: str
    # country: str
    # state: str
    # city: str
    # neighborhood: str
    # street: str
    # number: str

class UserCreate(UserSchema):
    password: SecretStr

class User(UserSchema):
    id: int
    update_at: datetime
    create_at: datetime

    class Config:
        orm_mode = True
