from app.database_repository import DataBaseRepository
import asyncio

class CacheRepo:
    def __init__(self, database_repository:DataBaseRepository) -> None:
        self.cache_store = database_repository.data_store 
        self.database_repository = database_repository
        self.hits = 0

    async def update_all_cache(self):
        await asyncio.sleep(0.0001)
        self.hits += 1
        self.cache_store = self.database_repository.data_store
        
    async def get_user_by_id(self, user_id):
        await asyncio.sleep(0.001)
        self.hits+=1
        try:
            return {
                "user_id": user_id,
                "user_name": self.cache_store[user_id]
            }
        except Exception as e:
            return None