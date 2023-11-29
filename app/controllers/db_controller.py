from app.database_repository import DataBaseRepository
from app.models.user import User
from app.caching.caching_service import CacheService
import asyncio

db = DataBaseRepository()
cache = CacheService(db) 

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

    
    async def get_user_by_id(self, userid:str, user_cache:bool=True):
        user = None
        if user_cache:
            user = await cache.get_user_by_id(userid)
        else:
            user = await db.get_user_by_id(userid)
        return user

        # Hillarious: I can't believe I coded this

        # if user:
        #     return user
        # else:
        #     return None
