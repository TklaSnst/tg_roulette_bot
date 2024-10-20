from pydantic import BaseModel


class CreateUser(BaseModel):
    name: str
    balance: float
    tg_id: int
