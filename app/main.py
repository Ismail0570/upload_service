from fastapi import FastAPI
from app.routers import upload

app = FastAPI(title="Upload Service")

app.include_router(upload.router)