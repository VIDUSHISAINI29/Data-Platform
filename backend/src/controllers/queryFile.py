from fastapi import HTTPException
import traceback
from src.services.queryFile import execute_sql_query_for_raw_file, transform_file, execute_sql_query_for_transformed_file

def execute_query_for_raw(
    file_name: str,
    query: str
):
    try:
        return execute_sql_query_for_raw_file(
            file_name,
            query
        )

    except HTTPException:
        raise

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"Query execution for raw file failed: {str(e)}"
        )

    
def execute_query_for_transformed(
    file_name: str,
    query: str
):
    try:
        return execute_sql_query_for_transformed_file(
            file_name,
            query
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Query execution for transformed file failed: {str(e)}"
        )

    
def transform_file_using_query(
    file_name: str,
    query: str
):
    try:
        return transform_file(
            file_name,
            query
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Query execution for transformation failed: {str(e)}"
        )