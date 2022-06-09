from typing import List
from src.utils.app_types import Id
from src.utils.pagination import Pagination
from src.schemas.user_schema import UserCreate, UserUpdate, User
from src.repositories.implementations.user_sqlalchemy_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository = UserRepository()):
        self.repository = repository

    def create(self, user: UserCreate) -> int:
        return self.repository.create(user)

    def read(self, id: Id) -> User:
        return self.repository.read(id)

    def update(self, id: Id, user: UserUpdate) -> None:
        self.repository.update(id, user)

    def delete(self, id: Id) -> None:
        self.repository.delete(id)

    def read_many(self, pagination: Pagination) -> List[User]:
        return self.repository.read_many(pagination)

    def count(self) -> int:
        return self.repository.count()
