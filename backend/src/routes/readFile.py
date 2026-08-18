from fastapi import APIRouter
from src.controllers.readFile import get_list_of_files, get_preview_of_file


read_file_router = APIRouter()

@read_file_router.get('/read-files')
def read_endpoint():
    files = get_list_of_files()
    return files    

# @read_file_router.get('/file-preview/{file_name}')
# def preview_endpoint(file_name:str):
#     file = get_preview_of_file(file_name)
#     print(file)
#     return file    

@read_file_router.get("/file-preview/{file_name}")
async def preview_endpoint(
    file_name: str,
    limit: int = 10
):
    return await get_preview_of_file(
        file_name,
        limit
    )