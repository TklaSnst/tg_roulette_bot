from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from database.database import async_session
from http.server import HTTPServer, SimpleHTTPRequestHandler
from database.crud import get_user_balance


router = APIRouter(
    tags=["pages"],
    prefix="/page",
)
templates = Jinja2Templates(directory="static")


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request, "test": "a"})
