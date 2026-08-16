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

    file = next((f for f in os.listdir(DATA_DIR) if f == "{file_name}"), None)
    return {file: file}
    



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
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse file: {str(e)}")


async def get_file_preview(file_name: str):
    file_bytes, extension = fetch_file_from_data_folder(file_name)
    df = process_file_to_df(file_bytes, extension)
    
    return {
        "columns": list(df.columns),
        "data": df.to_dict(orient="records")
    }