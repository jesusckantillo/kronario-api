from fastapi import APIRouter
from schemas.schemas import Majors, Classcodes, Teacher
from config.crud import crud
from typing import List

teachers = APIRouter()

@teachers.post("/teachers")
async def get_majors_classcodes(classcodes:List[str]):
    codes = [classcode for classcode in classcodes]
    teachers = crud.get_professors_by_classcodes(codes)
    return [Teacher(name=element[0],classcodes_name=element[1]) for element in teachers]