# -*- coding: utf-8 -*-
import uvicorn

from app.core import app
from app.core.config import get_env
from app.core.db.session import Base, engine
from app.v1.router.user_router import router as user_router

app.include_router(user_router)


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(engine)


@app.on_event("shutdown")
async def shutdown_event():
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", host=get_env().app_host, port=get_env().app_port)
