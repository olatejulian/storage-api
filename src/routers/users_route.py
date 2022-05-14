'''
from routers import users_route

app.include_router(users_route.router)
'''
from fastapi import APIRouter, Depends

from services.users_service import UserService
from utils.pagination import Pagination

router = APIRouter(prefix='/user', tags=['User Routes'])

@router.post('/')
async def create_user():
    return {'Users': 'Hello World'}

@router.get('/')
async def read_users(body: Pagination = Depends(Pagination)):
    return {'Users': 'Hello World'}

@router.get(':id')
async def read_user():
    pass

@router.patch(':id')
async def update_user():
    pass

@router.delete(':id')
async def delete_user():
    pass
