from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, SecretStr
from src.utils.app_types import Id
from src.utils.all_fields_optional import AllFieldsOptional

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    name: str

    def _fields(self):
        return {k: v.get_secret_value() if type(v) == SecretStr else v for k, v in self.__dict__.items() if v is not None}

    class Config:
        orm_mode = True

class UserCreate(UserSchema):
    password: SecretStr
    # password: str

class UserUpdate(UserSchema, metaclass=AllFieldsOptional):
    updated_at: Optional[datetime] = datetime.now()


class User(UserSchema):
    id: Id
    updated_at: datetime
    created_at: datetime
