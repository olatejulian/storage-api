from src.repositories.implementations.user_sqlalchemy_repository import UserRepository
from src.schemas.user_schema import UserCreate, User

class UserService:
    def __init__(self, repository: UserRepository = UserRepository()):
        self.repository = repository

    def create(self, user: UserCreate) -> int:
        return self.repository.create(user)

    def read(self, id: int) -> User:
        return self.repository.read(id)

    def update(self, id: int, user: User) -> None:
        self.repository.update(id, user)

    def delete(self, id: int) -> None:
        self.repository.delete(id)
