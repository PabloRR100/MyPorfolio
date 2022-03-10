from venv import create
from fastapi import FastAPI
import logging

from api.config import get_settings, Settings
from api.db import create_db_and_tables
from api.routes import company as company_router

SETTINGS = get_settings()
API_VERSION =SETTINGS.API_VERSION
logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(
        title="Portfolio API", 
        version=API_VERSION,
        on_startup=[create_db_and_tables]
    )

    app.include_router(
        company_router.router, prefix=f"/{API_VERSION}", tags=["Company"]
    )

    return app


app = create_app()

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")


if __name__ == "__main__":
    # This is for development purposes. It is not efficient to run real traffic.
    # The app in any env should be run by docker-entrypoint.sh.
    import uvicorn

    logger.info(f"Starting application on port {SETTINGS.APP_PORT}")

    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=SETTINGS.APP_PORT,
        debug=True,
        reload=True,
        reload_dirs=["/app"],
    )
