from fastapi import APIRouter
from index import upload_file_router

api_router = APIRouter()

api_router.include_router(upload_file_router, prefix="uploads")