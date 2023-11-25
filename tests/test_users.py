from fastapi.testclient import TestClient
from app.main import app
import asyncio
import httpx
client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Mf"}

async def async_test_users():
    async with httpx.AsyncClient() as async_client:
        tasks = []

        for i in range(1000):
            user_name = f"user_{i}"
            payload = {
                "user_name": user_name
            }
            url = "http://localhost:8000/user/"
            tasks.append(async_client.post(url, json=payload))

        responses = await asyncio.gather(*tasks)

        for response in responses:
            print("lodda")
            print(response.json())
            assert response.status_code == 200

asyncio.run(async_test_users())

if __name__ == "__main__":
    test_users()