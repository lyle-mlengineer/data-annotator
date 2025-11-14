from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles

from app.core.config import config
from app.core.logging import setup_logging
# from app.ui.v1 import ui
from app.core.worker import add


setup_logging()
app = FastAPI(title=config.APP_NAME, debug=config.DEBUG)

# app.include_router(ui.router)

app.mount("/static", StaticFiles(directory=config.STATIC_DIR), name="static")

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok"}

@app.get("/")
async def root(x: int = 2, y: int = 3):
    add.delay(x, y)
    return {"message": "Welcome to SautiFlow Labs Data Annotator API"}