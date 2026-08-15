from fastapi import HTTPException
from src.services.readFile import list_files
def get_list_of_files():
    try:
        files_list = list_files()
        return files_list
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
