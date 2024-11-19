from fastapi_users import schemas
from pydantic import BaseModel
from sqlalchemy import BigInteger


class UserRead(schemas.BaseUser[int]):
    tg_id: str
    tg_fullname: str
    balance: float
    is_superuser: bool


class UserCreate(BaseModel):
    tg_id: int
    tg_fullname: str
    balance: float
    is_superuser: bool


class UserUpdate(schemas.BaseUserUpdate):
    balance: float
    is_superuser: bool

