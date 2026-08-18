from fastapi import APIRouter 
from pydantic import BaseModel
from src.controllers.queryFile import execute_query

query_file_router = APIRouter()


class SQLQueryRequest(BaseModel):
    file_name: str
    query: str

@query_file_router.post('/query-file')
async def query_endpoint(request: SQLQueryRequest):
    return execute_query(
        request.file_name,
        request.query
    )


