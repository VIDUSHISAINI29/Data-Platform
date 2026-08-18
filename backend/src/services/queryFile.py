from pydantic import BaseModel
import os
from pathlib import Path
import io 
import pandas as pd
import duckdb
from fastapi import HTTPException
from src.services.readFile import dataframe_to_preview

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data" / "raw" 


def execute_sql_query(file_name: str, query: str):
    file_path = DATA_DIR / file_name

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    extension = file_path.suffix.lower()

    if extension == ".parquet":
        source = f"read_parquet('{file_path}')"

    elif extension == ".csv":
        source = f"read_csv_auto('{file_path}')"

    elif extension == ".json":
        source = f"read_json_auto('{file_path}')"

    else:
        raise HTTPException(
            status_code=400,
            detail="SQL querying is currently supported for Parquet, CSV and JSON files"
        )

    connection = duckdb.connect()

    try:
        connection.execute(f"""
            CREATE VIEW data AS 
                SELECT * FROM {source}
        """)

        df = connection.execute(query).df()

        return dataframe_to_preview(df)

    finally:
        connection.close()
    

