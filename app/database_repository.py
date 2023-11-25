import uuid
import time
import asyncio

class DataBaseRepository:
    def __init__(self,):
        self.data_store = dict()
        self.hits=0

    async def add_user(self, username: str):
        await asyncio.sleep(0.008)
        self.hits+=1
        id = str(uuid.uuid4())
        print(f"DB hit {self.hits}")
        self.data_store[id] = username

        return {"id": id, "username":username}