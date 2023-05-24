from fastapi import APIRouter
from schemas.schemas import Majors, Classcodes
from config.crud import crud
from typing import List

teachers = APIRouter()

@teachers.post("/teachers")
async def get_majors_classcodes(classcodes:List[str]):
    codes = [classcode for classcode in classcodes]
    return crud.get_professors_by_classcodes(codes)
    