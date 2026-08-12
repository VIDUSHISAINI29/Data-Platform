from fastapi import APIRouter
from src.routes.uploadFile import file_upload_router

api_router = APIRouter()

api_router.include_router(file_upload_router, prefix="/uploads")