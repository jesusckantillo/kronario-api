from fastapi import APIRouter
from schemas.schemas import Majors, Classcodes, Teacher
from src.Utils.utils import generate_short_id
from config.crud import crud
from typing import List

teachers = APIRouter()


@teachers.post("/teachers")
async def get_majors_classcodes(classcodes: List[Classcodes]):
    codes = [classcode.id for classcode in classcodes]
    professors = crud.get_professors_by_classcodes(codes)
    teachers_list = []
    for professor in professors:
        teacher_obj = {
            "name": professor[0],
            "category": professor[1],
            "id": generate_short_id()
        }
        teachers_list.append(teacher_obj)
    print(teachers_list)
    return teachers_list