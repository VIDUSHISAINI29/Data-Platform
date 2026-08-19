from fastapi import HTTPException
from src.services.queryFile import execute_sql_query, transform_file

def execute_query(
    file_name: str,
    query: str
):
    try:
        return execute_sql_query(
            file_name,
            query
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Query execution failed: {str(e)}"
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