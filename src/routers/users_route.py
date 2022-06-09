'''

'''
from fastapi import APIRouter, Depends

from src.utils.app_types import Id
from src.utils.pagination import Pagination
from src.services.users_service import UserService
from src.schemas.user_schema import UserCreate, UserUpdate, User

router = APIRouter(prefix='/users', tags=['User Routes'])

service = UserService()

# CRUD basic routes
@router.post('/')
async def create_user(user: UserCreate) -> int:
    return service.create(user)

@router.get('/{id}', response_model=User)
async def read_user(id: Id) -> User:
    return service.read(id)

@router.patch('/{id}')
async def update_user(id: Id, user: UserUpdate) -> None:
    service.update(id, user)

@router.delete('/{id}')
async def delete_user(id: Id) -> None:
    service.delete(id)

#complex routes
@router.get('/')
async def read_users(body: Pagination = Depends(Pagination)) -> list[User]:
    pass
