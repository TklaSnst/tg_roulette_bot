from fastapi_users import FastAPIUsers
from database.models import User
from .users.auth import auth_backend, get_user_manager
from fastapi import APIRouter

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
