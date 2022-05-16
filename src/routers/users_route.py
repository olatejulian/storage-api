'''

'''
from fastapi import APIRouter, Depends

from src.services.users_service import UserService
from src.schemas.user_schema import UserCreate, UserUpdate, User
from src.utils.pagination import Pagination

router = APIRouter(prefix='/users', tags=['User Routes'])

user_service = UserService()

# CRUD basic routes
@router.post('/')
async def create_user(user: UserCreate) -> int:
    return user_service.create(user)

@router.get('/{id}', response_model=User)
async def read_user(id: int) -> User:
    return user_service.read(id)

@router.patch('/{id}')
async def update_user(id: int, user: UserUpdate) -> None:
    user_service.update(id, user)

@router.delete('/{id}')
async def delete_user(id: int) -> None:
    user_service.delete(id)

#complex routes
@router.get('/')
async def read_users(body: Pagination = Depends(Pagination)) -> list[User]:
    pass
