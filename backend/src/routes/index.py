from fastapi import APIRouter
from src.routes.uploadFile import file_upload_router
from src.routes.readFile import read_file_router
from src.routes.queryFile import query_file_router

api_router = APIRouter()

api_router.include_router(file_upload_router, prefix="/uploads")
api_router.include_router(read_file_router, prefix="/reads")
api_router.include_router(query_file_router, prefix="/query")