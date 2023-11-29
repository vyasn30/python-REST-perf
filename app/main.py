from fastapi import FastAPI
from .routers import router
import uvicorn

app = FastAPI()
app.include_router(router)


@app.get("/")
async def index():
    return {"message" : "Hello Mf"}

# if __name__ == "__main__":
    # uvicorn.run(app, )