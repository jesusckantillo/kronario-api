from fastapi import APIRouter
from typing import List
from config.crud import crud

filters = APIRouter()

@filters.get("/filters")
async def get_filters():
    return {"filters"}