from datetime import datetime
from pydantic import BaseModel, EmailStr, SecretStr

class User(BaseModel):
    username: str
    password: SecretStr
    email: EmailStr
    name: str
    age: int
    gender: str
    create_at: datetime

    # zip_code: str
    # country: str
    # state: str
    # city: str
    # neighborhood: str
    # street: str
    # number: str
