from fastapi import FastAPI
from .routers import public_api, local_db

app = FastAPI(title="Test Task API")


app.include_router(public_api.router, prefix="/api/v1/public", tags=["Public API"])
app.include_router(local_db.router, prefix="/api/v1/local", tags=["Local DB"])
