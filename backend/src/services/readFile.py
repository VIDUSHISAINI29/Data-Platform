import os
from pathlib import Path
import io 
import pandas as pd
from fastapi import HTTPException

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data" / "raw" 

def list_files():
    """Lists all supported data files in the folder."""
    supported_extensions = (".csv", ".json", ".xlsx", ".xls", ".parquet")
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(supported_extensions)]
    return {"files": files}



## Reading Files to show on the frontend


def fetch_file_from_data_folder(file_name: str):

    file_path = os.path.join(DATA_DIR, file_name)

    if not os.path.isfile(file_path):
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    with open(file_path, "rb") as file:
        file_bytes = file.read()

    extension = file_name.rsplit(".", 1)[-1].lower()

    return file_bytes, extension


def process_file_to_df(file_bytes: bytes, extension: str) -> pd.DataFrame:
    try:
        file_stream = io.BytesIO(file_bytes)
        if extension == "csv":
            return pd.read_csv(file_stream)
        elif extension == "json":
            return pd.read_json(file_stream)
        elif extension == "parquet":
            return pd.read_parquet(file_stream)
        elif extension == "xls":
            return pd.read_excel(file_stream)
        elif extension == "xlsx":
            return pd.read_excel(file_stream)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse file: {str(e)}")


def get_file_preview(file_name: str):
    file_bytes, extension = fetch_file_from_data_folder(file_name)
    df = process_file_to_df(file_bytes, extension)
    
    return {
        "columns": list(df.columns),
        "data": df.to_dict(orient="records")
    }