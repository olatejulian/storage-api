from sqlalchemy import insert, select, update, delete
from src.schemas.user_schema import UserCreate
from src.repositories.interfaces.users_interface import IUserRepository
from src.repositories.models.user_sqlalchemy_model import UserModel
from src.repositories.implementations.sqlalchemy_session import Session

class UserRepository(IUserRepository):
    def __init__(self, session: Session = Session()):
        self.session = session

    def create(self, user: UserCreate) -> int:
        with self.session.begin() as session_transaction:
            new_user = UserModel(**user.dict())
            # self.session.execute(insert(new_user))
            self.session.add(new_user)
            # user_created = self.session.refresh(new_user)

        # return user_created.id

    def read(self, id: int) -> UserModel:
        with self.session.begin() as session:
            read_result = session.execute(select(UserModel).where(UserModel.id == id))

        return read_result

    def update(self, id: int, fields_to_update: UserModel) -> None:
        with self.session.begin() as session:
            values = fields_to_update.__dict__
            session.execute(update(UserModel).where(UserModel.id == id).values(**values))

    def delete(self, id: int) -> None:
        with self.session.begin() as session:
            session.execute(delete(UserModel).where(UserModel.id == id))
