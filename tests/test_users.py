from fastapi.testclient import TestClient
from app.main import app
import asyncio
import httpx
client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Mf"}

async def async_test_create_users(n_users: int):
    # Normal test client doesn't work for async tests. Use httpx's AsyncClient() 
    async with httpx.AsyncClient() as async_client:
        tasks = []

        for i in range(n_users):
            user_name = f"user_{i}"
            payload = {
                "user_id": str(i),
                "user_name": user_name
            }
            url = "http://localhost:8000/user/"
            tasks.append(async_client.post(url, json=payload))

        responses = await asyncio.gather(*tasks)

        for response in responses:
            assert response.status_code == 200

async def async_test_get_users(n_req:int):
    async with httpx.AsyncClient() as async_client:

        tasks = []

        for i in range(n_req):
            userid = str(i%100)
            url =f"http://localhost:8000/user/?userid={userid}"
            tasks.append(async_client.get(url))

        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response.json())
            assert response.status_code == 200


async def async_test_get_users_cached(n_req:int):
    async with httpx.AsyncClient() as async_client:

        tasks = []

        for i in range(n_req):
            userid = str(i%100)
            url =f"http://localhost:8000/user/cached/?userid={userid}"
            tasks.append(async_client.get(url))

        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response.json())
            assert response.status_code == 200

asyncio.run(async_test_create_users(100))
asyncio.run(async_test_get_users(1000))
asyncio.run(async_test_get_users_cached(1000))
