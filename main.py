import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.anagram.db import redis
from app.anagram.views import router_anagram
from app.device.db import engine
from app.device.views import router_device

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
app.include_router(router_anagram)
app.include_router(router_device)


@app.on_event('shutdown')
async def shutdown():
    await engine.dispose()
    await redis.close()
    await redis.wait_closed()


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, host='127.0.0.1', reload=True)
