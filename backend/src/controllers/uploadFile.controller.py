from fastapi import UploadFile, HTTPException
from services import upload_file_service


async def handle_file_upload(file: UploadFile):
    # Validation checks (like Express route validation)
    if not file.filename:
        raise HTTPException(status_code=400, detail="Invalid file name")

    try:
        # Pass the file deeper into the business logic layer (Service)
        saved_path = upload_file_service.save_raw_file(file)

        # Format the HTTP response (Like res.status(201).json(...))
        return {
            "status": "success",
            "message": "File processed successfully",
            "data": {"path": str(saved_path)},
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
