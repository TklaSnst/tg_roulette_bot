from pydantic import BaseModel


class Base(BaseModel):
    pass


class CreateUser(Base):
    name: str
    balance: float
    tg_id: int


class CreateGame(Base):
    user_tgid: int
    user_bet_amount: int
    user_bet_color: int
    win_color: str
