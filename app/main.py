from fastapi import FastAPI
from app.routes.main_route import main_router
from app.routes.user_route import user_router
from app.routes.signup_route import signup_router
from app.routes.login_route import login_router

app = FastAPI()

app.include_router(main_router)
app.include_router(user_router, prefix="/users")
app.include_router(signup_router, prefix="/signup")
app.include_router(login_router, prefix="/login")