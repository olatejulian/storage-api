from src.repositories.interfaces.users_interface import IUserRepository
from src.repositories.models.user_sqlalchemy_model import UserModel
from src.repositories.implementations.sqlalchemy_session import Session

class UserRepository(IUserRepository):
    def __init__(self, session: Session = Session()):
        self.session = session

    def create(self, user: UserModel) -> int:
        with self.session.begin() as session:
            create_result = session.add(user)

        return create_result.id

    def read(self, id: int) -> UserModel:
        with self.session.begin() as session:
            read_result = session.get(id)

        return read_result

    def update(self, id: int, fields_to_update: UserModel) -> None:
        with self.session.begin() as session:
            session.update(id, fields_to_update)

    def delete(self, id: int) -> None:
        with self.session.begin() as session:
            session.delete(id)
