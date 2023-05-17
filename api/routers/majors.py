from fastapi import APIRouter
from typing import List
from config.crud import crud
from schemas.schemas import Majors, MajorsRequest

majors = APIRouter()

@majors.get("/majors", response_model=List[Majors])
async def get_majors():
    db_majors = crud.get_majors()
    return [Majors(name=major.name,major_code=major.major_code) for major in db_majors] 
     
@majors.get("/majors/classcodes")
async def get_majors_classcodes(major_codes: List[str]):
    db_classcodes = []
    for major_code in major_codes:
        classcodes = crud.get_majors_classcodes(major_code)
        db_classcodes.append(classcodes)
    return db_classcodes