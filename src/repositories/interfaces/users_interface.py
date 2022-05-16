'''
Links:
------
https://breadcrumbscollector.tech/python-the-clean-architecture-in-2021/
'''
import abc
from src.schemas.user_schema import UserCreate, UserUpdate, User

class IUserRepository(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def create(self, user: UserCreate) -> int:
        pass

    @abc.abstractmethod
    def read(self, id: int) -> User:
        pass

    @abc.abstractmethod
    def update(self, id: int, user_update: UserUpdate) -> None:
        pass

    @abc.abstractmethod
    def delete(self, id: int) -> None:
        pass
