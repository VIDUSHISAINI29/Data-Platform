from fastapi import HTTPException
from src.services.queryFile import execute_sql_query

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