import logging

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.api import ping, summaries
from app.db import init_db
from app.views import home

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.mount('/app/static', StaticFiles(directory='app/static'), name='static')
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )
    application.include_router(home.router)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
