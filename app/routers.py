from fastapi import APIRouter
from app.models.user import User
from app.controllers.db_controller import DataBaseController
import asyncio

router = APIRouter()
controller = DataBaseController()

@router.post("/user/")
async def create_user(user: User):
    ret = await asyncio.gather(controller.add_user(user.user_name))
    return ret


@router.get("/users/")
async def get_all_users():
    return controller.get_all_users()