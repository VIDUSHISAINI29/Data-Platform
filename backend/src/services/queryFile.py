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
TRANSFORMED_DIR = ROOT / "data" / "transformed"

TRANSFORMED_DIR.mkdir(parents=True, exist_ok=True)



def execute_sql_query(
    file_name: str,
    query: str
):
    file_path = DATA_DIR / file_name

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    extension = file_path.suffix.lower()

    if extension == ".parquet":
        reader = f"read_parquet('{file_path}')"

    elif extension == ".csv":
        reader = f"read_csv_auto('{file_path}')"

    elif extension == ".json":
        reader = f"read_json_auto('{file_path}')"

    elif extension == ".xlsx":
        reader = f"read_xlsx('{file_path}')"
        
    elif extension == ".xls":
        reader = f"read_xlsx('{file_path}')"

    else:
        raise HTTPException(
            status_code=400,
            detail="Transformation currently supports Parquet, CSV and JSON"
        )

    output_path = (
        TRANSFORMED_DIR /
        f"{file_path.stem}_transformed.parquet"
    )

    connection = duckdb.connect()

    try:

        # Load selected file into DuckDB
        connection.execute(
            f"""
            CREATE TABLE data AS
            SELECT *
            FROM {reader}
            """
        )

        # Execute user's transformation
        connection.execute(query)

        # Save transformed table
        connection.execute(
            f"""
            COPY data
            TO '{output_path}'
            (FORMAT PARQUET)
            """
        )

        return {
            "message": "File transformed successfully",
            "file_name": output_path.name,
            "path": str(output_path)
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=f"Transformation failed: {str(e)}"
        )

    finally:
        connection.close()