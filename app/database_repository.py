import asyncio

class DataBaseRepository:
    def __init__(self,):
        self.data_store = {}
        self.hits=0

    async def add_user(self, username: str, userid: str):
        await asyncio.sleep(0.08)
        self.hits+=1
        self.data_store[userid] = username

        return {"id": userid, "username":username}

    def get_all_users(self):
        return self.data_store

    async def get_user_by_id(self, userid):
        await asyncio.sleep(0.08)
        self.hits+=1
        try:
            return {
            "user_id": userid,
            "user_name": self.data_store[userid]
        }
        except Exception as e:
            return None
