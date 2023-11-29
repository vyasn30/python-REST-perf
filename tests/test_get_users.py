from datetime import date
import datetime
from fastapi.testclient import TestClient
from app.main import app
import asyncio
import httpx

client = TestClient(app)

async def async_test_get_users(n_req:int):
    async with httpx.AsyncClient(timeout=10) as async_client:

        tasks = []

        for i in range(n_req):
            userid = str(i%100)
            url =f"http://localhost:8000/user/?userid={userid}"
            tasks.append(async_client.get(url))

        responses = await asyncio.gather(*tasks)

        

        for response in responses:
            assert response.status_code == 200

asyncio.run(async_test_get_users(1000))