from app.database_repository import DataBaseRepository
from app.caching.cache_repo import CacheRepo
import datetime
import asyncio

class CacheService:
    def __init__(
        self, 
        database_repository:DataBaseRepository,
        invalidation_ttl=0
    ):
        self.database_repository = database_repository
        self.cache_repo = CacheRepo(database_repository=database_repository)
        self.last_validated_at = None
        self.invalidation_ttl = invalidation_ttl

    async def update_all_cache(self):
        await self.cache_repo.update_all_cache()
        self.last_validated_at = datetime.datetime.now()

    async def get_user_by_id(self, user_id):
        user = await self.cache_repo.get_user_by_id(user_id)
        return user

    def auto_update(self):
        # Implement this later
        pass

    def lru_update(self):
        # Implement later
        pass

    def lfu_update(self):
        # Implement late
        pass

    


    