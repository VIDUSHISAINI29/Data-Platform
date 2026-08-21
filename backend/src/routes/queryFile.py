from fastapi import APIRouter 
from pydantic import BaseModel
from src.controllers.queryFile import execute_query_for_raw, execute_query_for_transformed, transform_file_using_query

query_file_router = APIRouter()


class SQLQueryRequest(BaseModel):
    file_name: str
    query: str

@query_file_router.post('/query-raw-file')
async def query_endpoint(request: SQLQueryRequest):
    return execute_query_for_raw(
        request.file_name,
        request.query
    )


@query_file_router.post('/query-transformed-file')
async def query_endpoint(request: SQLQueryRequest):
    return execute_query_for_transformed(
        request.file_name,
        request.query
    )

@query_file_router.post('/transform-file')
async def transform_using_query_endpoint(request: SQLQueryRequest):
    return transform_file_using_query(
        request.file_name,
        request.query
    )


