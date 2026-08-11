import shutil
from pathlib import Path
from fastapi import UploadFile, File

ROOT = Path(__file__).resolve().parent.parent

uploaded_file_path = ROOT / "data" / "raw" 

async def upload_file_service(file: UploadFile = File(...)):
    file_path = f"{uploaded_file_path}{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "File saved successfully"}