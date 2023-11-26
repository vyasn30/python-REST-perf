from app.database_repository import DataBaseRepository
from app.models.user import User
import asyncio

db = DataBaseRepository()
class DataBaseController:
    def __init__(self):
        pass

    async def add_user(self, username: str, userid:str):
        ret = await asyncio.gather(db.add_user(username=username, userid=userid))
        print(f"-------{ret}")
        return {"status": 200, "message": "User Created SuccessFully"}

    def get_all_users(self):
        print(f"In get all users ---------------")
        print(db.data_store)
        return db.data_store

    
    async def get_user_by_id(self, userid:str):
        user = await db.get_user_by_id(userid)

        if user:
            return user
        else:
            return None
