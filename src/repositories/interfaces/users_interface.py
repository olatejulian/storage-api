'''
Links:
------
https://breadcrumbscollector.tech/python-the-clean-architecture-in-2021/
'''
import abc
from models.user_model import UserModel

class IUserRepository(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def create(self, user: UserModel) -> int:
        pass

    @abc.abstractmethod
    def read(self, id: int) -> UserModel:
        pass

    @abc.abstractmethod
    def update(self, id: int, fields_to_update: UserModel) -> None:
        pass

    @abc.abstractmethod
    def delete(self, id: int) -> None:
        pass
