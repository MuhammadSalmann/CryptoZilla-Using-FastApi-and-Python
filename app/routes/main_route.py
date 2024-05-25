from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.models.user_model import User
from app.db import collection
from bson import ObjectId
from typing import List

main_router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@main_router.get("/")
def read_root(request: Request):
    user = request.cookies.get('user')
    return templates.TemplateResponse("index.html", {"request": request, "user": user})

@main_router.get("/admin")
async def read_root(request: Request):
    users = await collection.find().to_list(100)
    return templates.TemplateResponse("user-crud.html", {"request": request, "users": users})

@main_router.get("/dashboard")
def get_dashboard(request: Request):
    user = request.cookies.get('user')
    if not user:
        return RedirectResponse("/login", status_code=303)
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user})

@main_router.post("/select-account")
def select_account(request: Request, account_type: str = Form(...), account_size: str = Form(...)):
    user = request.cookies.get('user')
    if not user:
        return RedirectResponse("/login", status_code=303)
    
    response = RedirectResponse("/select-instruments", status_code=303)
    response.set_cookie("account_type", account_type)
    response.set_cookie("account_size", account_size)
    return response

@main_router.get("/select-instruments")
def get_select_instruments(request: Request):
    user = request.cookies.get('user')
    if not user:
        return RedirectResponse("/login", status_code=303)
    account_type = request.cookies.get('account_type')
    account_size = request.cookies.get('account_size')
    return templates.TemplateResponse("instrument.html", {"request": request, "user": user, "account_type": account_type, "account_size": account_size})

@main_router.post("/calculate-profit-loss")
async def calculate_profit_loss(request: Request, instrument: str = Form(...), amount: float = Form(...), buying_price: float = Form(...), current_price: float = Form(...)):
    user = request.cookies.get('user')
    profit_loss = (current_price - buying_price) * amount
    status = "Profit" if profit_loss > 0 else "Loss"
    return templates.TemplateResponse("result.html", {"request": request, "user": user, "instrument": instrument, "amount": amount, "buying_price": buying_price, "current_price": current_price, "profit_loss": profit_loss, "status": status})

@main_router.get("/logout")
def logout(request: Request):
    response = RedirectResponse("/", status_code=303)
    response.delete_cookie("user")
    response.delete_cookie("account_type")
    response.delete_cookie("account_size")
    return response




