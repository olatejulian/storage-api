from typing import List
from interface import implements
from src.utils.app_types import Id
from src.utils.pagination import Pagination
from sqlalchemy import select, update, delete
from src.schemas.user_schema import UserCreate, UserUpdate, User
from src.repositories.models.user_sqlalchemy_model import UserModel
from src.repositories.interfaces.users_interface import IUserRepository
from src.repositories.implementations.sessions.sqlalchemy_session import Session

class UserRepository(implements(IUserRepository)):
    def __init__(self, session = Session):
        self.session = session()

    def create(self, user: UserCreate) -> Id:
        with self.session.begin():
            new_user = UserModel(**user._fields())

            self.session.add(new_user)

            self.session.flush()

            return new_user.id

    def read(self, id: int) -> User:
        with self.session.begin():
            read_user = self.session.scalar(select(UserModel).where(UserModel.id == id))

            user = User(**read_user._fields())

            return user

    def update(self, id: int, user_update: UserUpdate) -> None:
        with self.session.begin():
            self.session.execute(update(UserModel).where(UserModel.id == id).values(**user_update._fields()))

    def delete(self, id: int) -> None:
        with self.session.begin():
            self.session.execute(delete(UserModel).where(UserModel.id == id))

    def read_many(self, pagination: Pagination) -> List[User]:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError
