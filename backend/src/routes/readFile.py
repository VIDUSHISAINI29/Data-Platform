from fastapi import APIRouter
from src.controllers.readFile import get_list_of_files

read_file_router = APIRouter()

@read_file_router.get('/read-files')
def read_endpoint():
    files = get_list_of_files()
    print(files)
    return files    