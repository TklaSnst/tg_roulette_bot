from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from database.database import async_session
from http.server import HTTPServer, SimpleHTTPRequestHandler
from database.crud import get_user_by_tg_id


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

