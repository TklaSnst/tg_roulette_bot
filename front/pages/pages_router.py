from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from database.database import async_session
from database import create_game, CreateGame, Game
from database.crud import get_user_by_tg_id, patch_user_balance, user_win, get_user_balance


router = APIRouter(
    tags=["pages"],
    prefix="/page",
)
templates = Jinja2Templates(directory="static")


@router.get("/base/")
async def get_base_page(request: Request, tg_id: int = 0):
    if tg_id:
        user = await get_user_by_tg_id(async_session, tg_id)
        return templates.TemplateResponse(
            "base.html", {"request": request, "username": user.tg_fullname, "user_balance": user.balance}
        )


@router.get("/dbrequest/")
async def db_request(request: Request, tgid: int, usr_bet: int, usr_btn: int, game_res: str):
    if tgid and usr_bet and usr_btn and game_res:
        game_to_create = CreateGame(
            user_tgid=tgid,
            user_bet_amount=usr_bet,
            user_bet_color=usr_btn,
            win_color=game_res
        )
        bal = await patch_user_balance(async_session=async_session, tg_id=tgid, bet=usr_bet)
        data = Game(**game_to_create.model_dump())
        await create_game(async_session=async_session, game=data)
        return bal
    else:
        return "miss something"


@router.get("/usr_win/")
async def user_win_handler(request: Request, tgid: int, usr_bet: int, coefficient: int):
    if tgid and usr_bet and coefficient:
        bal = await user_win(
            async_session=async_session,
            tg_id=tgid,
            bet=usr_bet,
            coeff=coefficient)
        return bal
    else:
        return "miss something"

