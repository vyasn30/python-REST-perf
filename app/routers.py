from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.user import User
from app.controllers.db_controller import DataBaseController
import asyncio

router = APIRouter()
controller = DataBaseController()

@router.post("/user/")
async def create_user(user: User):
    ret = await asyncio.gather(controller.add_user(user.user_name, userid=user.user_id))
    return ret


@router.get("/users/")
async def get_all_users():
    return controller.get_all_users()

@router.get("/user/")
async def get_user(userid):
    user = await asyncio.gather(controller.get_user_by_id(userid))
    if user:
        return user
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)
