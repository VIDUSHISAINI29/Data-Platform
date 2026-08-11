from fastapi import APIRouter, UploadFile, File
from controllers import handle_file_upload

file_upload_router = APIRouter()

@file_upload_router.post('/upload-file')
async def upload_endpoint(file: UploadFile = File(...)):
    # Direct function call
    return await handle_file_upload(file)